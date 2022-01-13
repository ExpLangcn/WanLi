# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Author: Mauro Soria

import gc
import os
import sys
import time
import re
import threading

from urllib.parse import urljoin, urlparse
from queue import Queue

from lib.connection.requester import Requester
from lib.connection.request_exception import RequestException
from lib.core.dictionary import Dictionary
from lib.core.fuzzer import Fuzzer
from lib.core.raw import Raw
from lib.core.report_manager import Report, ReportManager
from lib.utils.file import FileUtils
from lib.utils.fmt import clean_filename
from lib.utils.size import human_size
from lib.utils.timer import Timer


class SkipTargetInterrupt(Exception):
    pass


MAJOR_VERSION = 0
MINOR_VERSION = 4
REVISION = 2
VERSION = {
    "MAYOR_VERSION": MAJOR_VERSION,
    "MINOR_VERSION": MINOR_VERSION,
    "REVISION": REVISION,
}


class EmptyReportManager(object):
    def __init__(self):
        pass

    def update_report(self, *args):
        pass


class EmptyReport(object):
    def __init__(self):
        pass

    def add_result(self, *args):
        pass


class EmptyTimer(object):
    def __init__(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass


class Controller(object):
    def __init__(self, script_path, arguments, output):
        global VERSION
        program_banner = (
            open(FileUtils.build_path(script_path, "banner.txt"))
            .read()
            .format(**VERSION)
        )

        self.directories = Queue()
        self.script_path = script_path
        self.arguments = arguments
        self.output = output
        self.pass_dirs = ["/"]

        if arguments.raw_file:
            raw = Raw(arguments.raw_file, arguments.scheme)
            self.url_list = [raw.url]
            self.httpmethod = raw.method
            self.data = raw.body
            self.headers = raw.headers
        else:
            default_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept-Language": "*",
                "Accept-Encoding": "*",
                "Keep-Alive": "timeout=15, max=1000",
                "Cache-Control": "max-age=0",
            }

            self.url_list = arguments.url_list
            self.httpmethod = arguments.httpmethod.lower()
            self.data = arguments.data
            self.headers = {**default_headers, **arguments.headers}
            if arguments.cookie:
                self.headers["Cookie"] = arguments.cookie
            if arguments.useragent:
                self.headers["User-Agent"] = arguments.useragent

        self.recursion_depth = arguments.recursion_depth

        if arguments.logs_location and self.validate_path(arguments.logs_location):
            self.logs_path = FileUtils.build_path(arguments.logs_location)
        elif self.validate_path(self.script_path):
            self.logs_path = FileUtils.build_path(self.script_path, "logs")
            if not FileUtils.exists(self.logs_path):
                FileUtils.create_directory(self.logs_path)

        if arguments.output_location and self.validate_path(arguments.output_location):
            self.report_path = FileUtils.build_path(arguments.output_location)
        elif self.validate_path(self.script_path):
            self.report_path = FileUtils.build_path(self.script_path, "reports")
            if not FileUtils.exists(self.report_path):
                FileUtils.create_directory(self.report_path)

        self.blacklists = Dictionary.generate_blacklists(arguments.extensions, self.script_path)
        self.extensions = arguments.extensions
        self.prefixes = arguments.prefixes
        self.suffixes = arguments.suffixes
        self.threads_count = arguments.threads_count
        self.output_file = arguments.output_file
        self.output_format = arguments.output_format
        self.include_status_codes = arguments.include_status_codes
        self.exclude_status_codes = arguments.exclude_status_codes
        self.exclude_sizes = arguments.exclude_sizes
        self.exclude_texts = arguments.exclude_texts
        self.exclude_regexps = arguments.exclude_regexps
        self.exclude_redirects = arguments.exclude_redirects
        self.replay_proxy = arguments.replay_proxy
        self.recursive = self.arguments.recursive
        self.deep_recursive = arguments.deep_recursive
        self.force_recursive = arguments.force_recursive
        self.recursion_status_codes = arguments.recursion_status_codes
        self.minimum_response_size = arguments.minimum_response_size
        self.maximum_response_size = arguments.maximum_response_size
        self.scan_subdirs = arguments.scan_subdirs
        self.exclude_subdirs = arguments.exclude_subdirs
        self.full_url = arguments.full_url
        self.skip_on_status = arguments.skip_on_status
        self.exit_on_error = arguments.exit_on_error
        self.maxtime = arguments.maxtime

        self.dictionary = Dictionary(
            paths=arguments.wordlist,
            extensions=arguments.extensions,
            suffixes=arguments.suffixes,
            prefixes=arguments.prefixes,
            lowercase=arguments.lowercase,
            uppercase=arguments.uppercase,
            capitalization=arguments.capitalization,
            force_extensions=arguments.force_extensions,
            exclude_extensions=arguments.exclude_extensions,
            no_extension=arguments.no_extension,
            only_selected=arguments.only_selected
        )

        self.jobs_count = len(self.url_list) * (
            len(self.scan_subdirs) if self.scan_subdirs else 1
        )
        self.current_job = 0
        self.error_log = None
        self.error_log_path = None
        self.threads_lock = threading.Lock()
        self.batch = False
        self.batch_session = None

        self.report_manager = EmptyReportManager()
        self.report = EmptyReport()
        self.timer = EmptyTimer()

        self.output.header(program_banner)
        self.print_config()

        if arguments.use_random_agents:
            self.random_agents = FileUtils.get_lines(
                FileUtils.build_path(script_path, "db", "user-agents.txt")
            )

        if arguments.autosave_report or arguments.output_file:
            self.setup_reports()

        self.setup_error_logs()
        self.output.error_log_file(self.error_log_path)

        if self.maxtime:
            threading.Thread(target=self.time_monitor, daemon=True).start()

        try:
            for url in self.url_list:
                try:
                    gc.collect()
                    url = url if url.endswith("/") else url + "/"
                    self.output.set_target(url, arguments.scheme)

                    try:
                        self.requester = Requester(
                            url,
                            max_pool=arguments.threads_count,
                            max_retries=arguments.max_retries,
                            timeout=arguments.timeout,
                            ip=arguments.ip,
                            proxy=arguments.proxy,
                            proxylist=arguments.proxylist,
                            redirect=arguments.redirect,
                            request_by_hostname=arguments.request_by_hostname,
                            httpmethod=self.httpmethod,
                            data=self.data,
                            scheme=arguments.scheme,
                        )

                        for key, value in self.headers.items():
                            self.requester.set_header(key, value)

                        if arguments.auth:
                            self.requester.set_auth(arguments.auth_type, arguments.auth)

                        # Test request to see if server is up
                        self.requester.request("")

                        if arguments.autosave_report or arguments.output_file:
                            self.report = Report(self.requester.host, self.requester.port, self.requester.protocol, self.requester.base_path)

                    except RequestException as e:
                        self.output.error(e.args[0]["message"])
                        raise SkipTargetInterrupt

                    if arguments.use_random_agents:
                        self.requester.set_random_agents(self.random_agents)

                    # Initialize directories Queue with start Path
                    self.base_path = self.requester.base_path
                    self.status_skip = None

                    if not self.scan_subdirs:
                        self.directories.put("")

                    for subdir in self.scan_subdirs:
                        self.directories.put(subdir)
                        self.pass_dirs.append(subdir)

                    match_callbacks = [self.match_callback]
                    not_found_callbacks = [self.not_found_callback]
                    error_callbacks = [self.error_callback, self.append_error_log]

                    self.fuzzer = Fuzzer(
                        self.requester,
                        self.dictionary,
                        suffixes=arguments.suffixes,
                        prefixes=arguments.prefixes,
                        exclude_response=arguments.exclude_response,
                        threads=arguments.threads_count,
                        delay=arguments.delay,
                        maxrate=arguments.maxrate,
                        match_callbacks=match_callbacks,
                        not_found_callbacks=not_found_callbacks,
                        error_callbacks=error_callbacks,
                    )
                    try:
                        self.prepare()
                    except RequestException as e:
                        self.output.error(e.args[0]["message"])
                        raise SkipTargetInterrupt

                except SkipTargetInterrupt:
                    self.report.completed = True
                    continue

        except KeyboardInterrupt:
            self.output.error("\nCanceled by the user")
            exit(0)

        finally:
            self.error_log.close()

        self.output.warning("\nTask Completed")

    # Print dirsearch metadata (threads, HTTP method, ...)
    def print_config(self):
        self.output.config(
            ', '.join(self.extensions),
            ', '.join(self.prefixes),
            ', '.join(self.suffixes),
            str(self.threads_count),
            str(len(self.dictionary)),
            str(self.httpmethod),
        )

    def time_monitor(self):
        self.timer = Timer()
        self.timer.count(self.maxtime)
        self.close("\nCanceled because the runtime exceeded the maximal set by user")

    # Create error log file
    def setup_error_logs(self):
        file_name = "errors-{0}.log".format(time.strftime("%y-%m-%d_%H-%M-%S"))
        self.error_log_path = FileUtils.build_path(
            self.logs_path, file_name
        )

        try:
            self.error_log = open(self.error_log_path, "w")
        except PermissionError:
            self.output.error(
                "Couldn't create the error log. Try running again with highest permission"
            )
            sys.exit(1)

    # Create batch report folder
    def setup_batch_reports(self):
        self.batch = True
        if not self.output_file:
            self.batch_session = "BATCH-{0}".format(time.strftime("%y-%m-%d_%H-%M-%S"))
            self.batch_directory_path = FileUtils.build_path(
                self.report_path, self.batch_session
            )

            if not FileUtils.exists(self.batch_directory_path):
                FileUtils.create_directory(self.batch_directory_path)

                if not FileUtils.exists(self.batch_directory_path):
                    self.output.error(
                        "Couldn't create batch folder at {}".format(self.batch_directory_path)
                    )
                    sys.exit(1)

    # Get file extension for report format
    def get_output_extension(self):
        if self.output_format and self.output_format not in ["plain", "simple"]:
            return ".{0}".format(self.output_format)
        else:
            return ".txt"

    # Create report file
    def setup_reports(self):
        if self.output_file:
            output_file = FileUtils.get_abs_path(self.output_file)
            self.output.output_file(output_file)
        else:
            if len(self.url_list) > 1:
                self.setup_batch_reports()
                filename = "BATCH"
                filename += self.get_output_extension()
                directory_path = self.batch_directory_path
            else:
                parsed = urlparse(self.url_list[0])
                filename = (
                    "{}_".format(parsed.path)
                )
                filename += time.strftime("%y-%m-%d_%H-%M-%S")
                filename += self.get_output_extension()
                directory_path = FileUtils.build_path(
                    self.report_path, clean_filename(parsed.netloc)
                )

            filename = clean_filename(filename)
            output_file = FileUtils.build_path(directory_path, filename)

            if FileUtils.exists(output_file):
                i = 2
                while FileUtils.exists(output_file + "_" + str(i)):
                    i += 1

                output_file += "_" + str(i)

            if not FileUtils.exists(directory_path):
                FileUtils.create_directory(directory_path)

                if not FileUtils.exists(directory_path):
                    self.output.error(
                        "Couldn't create the reports folder at {}".format(directory_path)
                    )
                    sys.exit(1)

            self.output.output_file(output_file)

        if self.output_file and self.output_format:
            self.report_manager = ReportManager(self.output_format, self.output_file)
        elif self.output_format:
            self.report_manager = ReportManager(self.output_format, output_file)
        else:
            self.report_manager = ReportManager("plain", output_file)

    # Check if given path is valid (can read/write)
    def validate_path(self, path):
        if not FileUtils.exists(path):
            self.output.error("{0} does not exist".format(path))
            exit(1)

        if FileUtils.exists(path) and not FileUtils.is_dir(path):
            self.output.error("{0} is a file, should be a directory".format(path))
            exit(1)

        if not FileUtils.can_write(path):
            self.output.error("Directory {0} is not writable".format(path))
            exit(1)

        return True

    # Validate the response by different filters
    def valid(self, path):
        if not path:
            return False

        if path.status in self.exclude_status_codes:
            return False

        if self.include_status_codes and path.status not in self.include_status_codes:
            return False

        if self.blacklists.get(path.status) and path.path in self.blacklists.get(path.status):
            return False

        if self.exclude_sizes and human_size(path.length).strip() in self.exclude_sizes:
            return False

        if self.minimum_response_size and self.minimum_response_size > path.length:
            return False

        if self.maximum_response_size and self.maximum_response_size < path.length:
            return False

        for exclude_text in self.exclude_texts:
            if exclude_text in path.body:
                return False

        for exclude_regexp in self.exclude_regexps:
            if (
                re.search(exclude_regexp, path.body)
                is not None
            ):
                return False

        for exclude_redirect in self.exclude_redirects:
            if path.redirect and (
                (
                    re.match(exclude_redirect, path.redirect) is not None
                ) or (
                    exclude_redirect in path.redirect
                )
            ):
                return False

        return True

    # Callback for found paths
    def match_callback(self, path):
        self.index += 1

        for status in self.skip_on_status:
            if path.status == status:
                self.status_skip = status
                return

        if not self.valid(path):
            del path
            return

        added_to_queue = False

        if (
                any([self.recursive, self.deep_recursive, self.force_recursive])
        ) and (
                not self.recursion_status_codes or path.status in self.recursion_status_codes
        ):
            if path.redirect:
                added_to_queue = self.add_redirect_directory(path)
            else:
                added_to_queue = self.add_directory(path.path)

        self.output.status_report(
            path.path, path.response, self.full_url, added_to_queue
        )

        if self.replay_proxy:
            self.requester.request(path.path, proxy=self.replay_proxy)

        new_path = self.current_directory + path.path

        self.report.add_result(new_path, path.status, path.response)
        self.report_manager.update_report(self.report)

        del path

    # Callback for invalid paths
    def not_found_callback(self, path):
        self.index += 1
        self.output.last_path(
            self.index,
            len(self.dictionary),
            self.current_job,
            self.jobs_count,
            self.fuzzer.stand_rate,
        )
        del path

    # Callback for errors while fuzzing
    def error_callback(self, path, error_msg):
        if self.exit_on_error:
            self.close("\nCanceled due to an error")

        else:
            self.output.add_connection_error()

    # Write error to log file
    def append_error_log(self, path, error_msg):
        with self.threads_lock:
            line = time.strftime("[%y-%m-%d %H:%M:%S] - ")
            line += self.requester.base_url + self.base_path + self.current_directory + path + " - " + error_msg
            self.error_log.write(os.linesep + line)
            self.error_log.flush()

    # Handle CTRL+C
    def handle_pause(self, message):
        self.output.warning(message)
        self.timer.pause()
        self.fuzzer.pause()

        Timer.wait(self.fuzzer.is_stopped)

        while True:
            msg = "[q]uit / [c]ontinue"

            if not self.directories.empty():
                msg += " / [n]ext"

            if len(self.url_list) > 1:
                msg += " / [s]kip target"

            self.output.in_line(msg + ": ")

            option = input()

            if option.lower() == "q":
                self.close("\nCanceled by the user")

            elif option.lower() == "c":
                self.timer.resume()
                self.fuzzer.resume()
                return

            elif option.lower() == "n" and not self.directories.empty():
                self.timer.resume()
                self.fuzzer.stop()
                return

            elif option.lower() == "s" and len(self.url_list) > 1:
                self.timer.resume()
                raise SkipTargetInterrupt

    # Monitor the fuzzing process
    def process_paths(self):
        while True:
            try:
                while not self.fuzzer.wait(0.25):
                    # Check if the "skip status code" was returned
                    if self.status_skip:
                        self.close(
                            "\nSkipped the target due to {0} status code".format(self.status_skip),
                            skip=True
                        )
                break

            except KeyboardInterrupt:
                self.handle_pause("CTRL+C detected: Pausing threads, please wait...")

    # Preparation between subdirectory scans
    def prepare(self):
        while not self.directories.empty():
            gc.collect()
            self.current_job += 1
            self.index = 0
            self.current_directory = self.directories.get()
            self.output.warning(
                "[{1}] Starting: {0}".format(
                    self.current_directory, time.strftime("%H:%M:%S")
                )
            )
            self.fuzzer.requester.base_path = self.output.base_path = self.base_path + self.current_directory
            self.fuzzer.start()
            self.process_paths()

        self.report.completed = True

    # Add directory to the recursion queue
    def add_directory(self, path):
        dirs = []
        added = False
        path = path.split("?")[0].split("#")[0]
        full_path = self.current_directory + path

        if any([path.startswith(directory) for directory in self.exclude_subdirs]):
            return False

        # Avoid paths contain consecutive slashes, we haven't had good handler for it yet
        if self.deep_recursive and "//" not in path:
            for i in range(1, path.count("/")):
                dir = self.current_directory + "/".join(path.split("/")[:i]) + "/"
                dirs.append(dir)

        if self.force_recursive:
            if not full_path.endswith("/"):
                full_path += "/"
            dirs.append(full_path)
        elif self.recursive and full_path.endswith("/"):
            dirs.append(full_path)

        for dir in list(set(dirs)):
            if dir in self.pass_dirs:
                continue
            elif self.recursion_depth and dir.count("/") > self.recursion_depth:
                continue

            self.directories.put(dir)
            self.pass_dirs.append(dir)

            self.jobs_count += 1
            added = True

        return added

    # Resolve the redirect and add the path to the recursion queue
    # if it's a subdirectory of the current URL
    def add_redirect_directory(self, path):
        base_path = "/" + self.base_path + self.current_directory + path.path

        redirect_url = urljoin(self.requester.base_url, path.redirect)
        redirect_path = urlparse(redirect_url).path

        if redirect_path == base_path + "/":
            path = redirect_path[len(self.base_path + self.current_directory) + 1:]

            return self.add_directory(path)

        return False

    def close(self, msg=None, skip=False):
        self.fuzzer.stop()
        self.output.error(msg)
        if skip:
            raise SkipTargetInterrupt

        self.report_manager.update_report(self.report)
        exit(0)
