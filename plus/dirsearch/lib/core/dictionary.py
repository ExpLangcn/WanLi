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

import re
import threading

from lib.utils.fmt import safequote, uniq, lowercase, uppercase, capitalize
from lib.utils.file import File, FileUtils


class Dictionary(object):

    def __init__(
        self,
        paths,
        extensions,
        suffixes=None,
        prefixes=None,
        lowercase=False,
        uppercase=False,
        capitalization=False,
        force_extensions=False,
        exclude_extensions=[],
        no_extension=False,
        only_selected=False,
    ):

        self.entries = []
        self.current_index = 0
        self.condition = threading.Lock()
        self._extensions = extensions
        self._exclude_extensions = exclude_extensions
        self._prefixes = prefixes
        self._suffixes = suffixes
        self._paths = paths
        self._force_extensions = force_extensions
        self._no_extension = no_extension
        self._only_selected = only_selected
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.capitalization = capitalization
        self.dictionary_files = [File(path) for path in self.paths]
        self.generate()

    @property
    def extensions(self):
        return self._extensions

    @extensions.setter
    def extensions(self, value):
        self._extensions = value

    @property
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, paths):
        self._paths = paths

    """
    Dictionary.generate() behaviour

    Classic dirsearch wordlist:
      1. If %EXT% keyword is present, append one with each extension REPLACED.
      2. If the special word is no present, append line unmodified.

    Forced extensions wordlist (NEW):
      This type of wordlist processing is a mix between classic processing
      and DirBuster processing.
          1. If %EXT% keyword is present in the line, immediately process as "classic dirsearch" (1).
          2. If the line does not include the special word AND is NOT terminated by a slash,
            append one with each extension APPENDED (line.ext) and ONLYE ONE with a slash.
          3. If the line does not include the special word and IS ALREADY terminated by slash,
            append line unmodified.
    """

    def generate(self):
        reext = re.compile(r"\%ext\%", re.IGNORECASE).sub
        result = []

        # Enable to use multiple dictionaries at once
        for dict_file in self.dictionary_files:
            for line in uniq(dict_file.get_lines(), filt=True):
                # Skip comments
                if line.startswith("#"):
                    continue

                if line.startswith("/"):
                    line = line[1:]

                if self._no_extension:
                    line = line[0] + line[1:].split(".")[0]
                    # Skip dummy paths
                    if line == ".":
                        continue

                # Skip if the path contains excluded extensions
                if self._exclude_extensions and (
                    any(["." + extension in line for extension in self._exclude_extensions])
                ):
                    continue

                # Classic dirsearch wordlist processing (with %EXT% keyword)
                if "%ext%" in line.lower():
                    for extension in self._extensions:
                        newline = reext(extension, line)
                        result.append(newline)

                # If forced extensions is used and the path is not a directory ... (terminated by /)
                # process line like a forced extension.
                elif self._force_extensions and not line.rstrip().endswith("/") and "." not in line:
                    for extension in self._extensions:
                        result.append(line + "." + extension)

                    result.append(line)
                    result.append(line + "/")

                # Append line unmodified.
                else:
                    if not self._only_selected or any(
                        [line.endswith("." + extension) for extension in self.extensions]
                    ):
                        result.append(line)

        # Some custom changes
        for entry in uniq(result):
            entries = [entry]
            for pref in self._prefixes:
                if not entry.startswith(pref):
                    entries.append(pref + entry)
            for suff in self._suffixes:
                if not entry.endswith("/") and not entry.endswith(suff):
                    entries.append(entry + suff)

            if self.lowercase:
                self.entries.extend(lowercase(entries))
            elif self.uppercase:
                self.entries.extend(uppercase(entries))
            elif self.capitalization:
                self.entries.extend(capitalize(entries))
            else:
                self.entries.extend(entries)

        del result

    # Get ignore paths for status codes.
    # More information: https://github.com/maurosoria/dirsearch#Blacklist
    @staticmethod
    def generate_blacklists(extensions, script_path):
        reext = re.compile(r"\%ext\%", re.IGNORECASE).sub
        blacklists = {}

        for status in [400, 403, 500]:
            blacklist_file_name = FileUtils.build_path(script_path, "db")
            blacklist_file_name = FileUtils.build_path(
                blacklist_file_name, "{}_blacklist.txt".format(status)
            )

            if not FileUtils.can_read(blacklist_file_name):
                # Skip if cannot read file
                continue

            blacklists[status] = []

            for line in FileUtils.get_lines(blacklist_file_name):
                # Skip comments
                if line.lstrip().startswith("#"):
                    continue

                if line.startswith("/"):
                    line = line[1:]

                # Classic dirsearch blacklist processing (with %EXT% keyword)
                if "%ext%" in line.lower():
                    for extension in extensions:
                        entry = reext.sub(extension, line)
                        blacklists[status].append(entry)

                # Forced extensions is not used here because -r is only used for wordlist,
                # applying in blacklist may create false negatives

                else:
                    blacklists[status].append(line)

        return blacklists

    def next_with_index(self, base_path=None):
        self.condition.acquire()

        try:
            result = self.entries[self.current_index]

        except IndexError:
            self.condition.release()
            raise StopIteration

        self.current_index = self.current_index + 1
        current_index = self.current_index
        self.condition.release()
        return current_index, result

    def __next__(self, base_path=None):
        _, path = self.next_with_index(base_path)
        return safequote(path)

    def reset(self):
        self.condition.acquire()
        self.current_index = 0
        self.condition.release()

    def __len__(self):
        return len(self.entries)
