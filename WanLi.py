# coding=utf-8

import os
import sys
import cmd2
import cmd2 as cmd
import lib.cmd.wanli
import config.config
from random import randint
from rich.table import Table
from datetime import datetime
from rich.console import Console
from rich.highlighter import Highlighter
from os import system, name
from cmd2 import Cmd2ArgumentParser, with_argparser

console = Console()


class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)


rainbow = RainbowHighlighter()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        console.print(rainbow('''
        ██╗    ██╗ █████╗ ███╗   ██╗    ██╗     ██╗
        ██║    ██║██╔══██╗████╗  ██║    ██║     ██║
        ██║ █╗ ██║███████║██╔██╗ ██║    ██║     ██║
        ██║███╗██║██╔══██║██║╚██╗██║    ██║     ██║
        ╚███╔███╔╝██║  ██║██║ ╚████║    ███████╗██║
         ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝'''))
        console.print('''
                                        [green]---Info：ExpLang''')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        console.print(rainbow('''
        ██╗    ██╗ █████╗ ███╗   ██╗    ██╗     ██╗
        ██║    ██║██╔══██╗████╗  ██║    ██║     ██║
        ██║ █╗ ██║███████║██╔██╗ ██║    ██║     ██║
        ██║███╗██║██╔══██║██║╚██╗██║    ██║     ██║
        ╚███╔███╔╝██║  ██║██║ ╚████║    ███████╗██║
         ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝'''))
        console.print('''
                                        [green]---Info：ExpLang''')

CVE_list = []

def search(path, keyword):
    content = os.listdir(path)
    for each in content:
        each_path = path + os.sep + each
        if keyword in each:
            CVE_list.append(each_path)
        if os.path.isdir(each_path):
            search(each_path, keyword)


class newcmd(cmd.Cmd):

    prompt = config.config.TITLE  # 自定义交互式提示字符串

    # 自定义欢迎语
    console.print(rainbow('''
        ██╗    ██╗ █████╗ ███╗   ██╗    ██╗     ██╗
        ██║    ██║██╔══██╗████╗  ██║    ██║     ██║
        ██║ █╗ ██║███████║██╔██╗ ██║    ██║     ██║
        ██║███╗██║██╔══██║██║╚██╗██║    ██║     ██║
        ╚███╔███╔╝██║  ██║██║ ╚████║    ███████╗██║
         ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝'''))
    console.print('''
                                        [green]---Info：ExpLang''')

    # ----------------------------------------分割----------------------------------------
    # 定义-h内容
    dirscan_parser = Cmd2ArgumentParser()
    dirscan_parser.add_argument(
        "url", help="扫描\033[1;37;34m单个\033[0mWeb应用敏感文件及敏感地址，dirscan \033[34mhttps://www.baidu.com/\033[0m")
    # 调用dirsearch对WEB应用进行敏感文件及敏感地址扫描

    @cmd2.with_argparser(dirscan_parser)
    def do_dirscan(self, args):
        '''扫描\033[1;37;34m单个\033[0mWeb应用敏感文件及敏感地址，dirscan \033[34mhttps://www.baidu.com/\033[0m'''
        if args.url != "":
            lib.cmd.wanli.dirscan(args.url)

    # ----------------------------------------分割----------------------------------------
    # 定义-h内容
    domain_parser = Cmd2ArgumentParser()
    domain_parser.add_argument(
        "domain", help="扫描\033[1;37;34m单个\033[0m主域名的相关域名及子域名，domain \033[34mbaidu.com\033[0m")
    # 调用subfinder及httpx进行子域名和相关域名扫描

    @cmd2.with_argparser(domain_parser)
    def do_domain(self, args):
        '''扫描\033[1;37;34m单个\033[0m主域名的相关域名及子域名，domain \033[34mbaidu.com\033[0m'''
        if args.domain != "":
            lib.cmd.wanli.domain(args.domain)

    # ----------------------------------------分割----------------------------------------
    # 定义-h内容
    ddir_parser = Cmd2ArgumentParser()
    ddir_parser.add_argument(
        "domain", help="扫描\033[1;37;34m单个\033[0m主域名的相关域名及子域名的敏感文件及敏感地址，ddir \033[34mbaidu.com\033[0m")
    # 先进行子域名检测，检测结果进行目录扫描

    @cmd2.with_argparser(ddir_parser)
    def do_ddir(self, args):
        '''扫描\033[1;37;34m单个\033[0m主域名的相关域名及子域名的敏感文件及敏感地址，ddir \033[34mbaidu.com\033[0m'''
        if args.domain != "":
            lib.cmd.wanli.ddir(args.domain)

    # ----------------------------------------分割----------------------------------------
    # 定义-h内容
    pocscan_parser = Cmd2ArgumentParser()
    pocscan_parser.add_argument("-s", nargs='?', help="搜索")
    pocscan_parser.add_argument("-u", nargs='?', help="扫描单个")
    pocscan_parser.add_argument("-l", nargs='?', help="扫描多个")
    pocscan_parser.add_argument("-t", nargs='?', help="指定漏洞", completer=cmd2.Cmd.shell_cmd_complete)
    # 先进行子域名检测，检测结果进行目录扫描

    @cmd2.with_argparser(pocscan_parser)
    def do_pocscan(self, args):
        '''扫描\033[1;37;34m单个\033[0m或\033[1;37;34m多个\033[0mWEB应用漏洞，可\033[1;37;34m指定\033[0m漏洞或批量漏洞，\033[1;37;34m批量\033[0m漏洞请使用“*.yaml”'''
        table = Table()
        if args.s:
            search('./lib/POC', args.s)
            table.add_column('[red]Name')
            table.add_column('Path')
            for i in CVE_list:
                table.add_row(args.s, i)
            console.print(table)
            CVE_list.clear()
        if args.u and args.t:
            console.print("[bold green][+][/bold green] [bold cyan]即将扫描 " + str(args.u) + " 的漏洞.")
            console.print("[bold green][+][/bold green] [bold cyan]正在准备扫描中...")
            datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            system(config.config.nuclei + r" -u " + str(args.u) + " -t '" + str(args.t) + "' -silent -nts -o logs/pocscan_" + datatime + r"_ok.txt -me logs/pocscan" + datatime + r"_md/")
        if args.l and args.t:
            f = open(args.l, "r", encoding="UTF-8") 
            for line in f.readlines():
                line = line.split()
                for i in line:
                    console.print("[bold green][+][/bold green] [bold cyan]即将扫描 " + str(i) + " 的漏洞.")
                    console.print("[bold green][+][/bold green] [bold cyan]正在准备扫描中...")
                    datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                    system(config.config.nuclei + r" -u " + str(i) + " -t '" + str(args.t) + "' -silent -nts -o logs/pocscan_" + datatime + r"_ok.txt -me logs/pocscan_" + datatime + r"_md/")
            

    # ----------------------------------------分割----------------------------------------
    # 当无法识别输入的command时调用该方法；
    def default(self, line):
        console.print(
            "[bold red][-][/bold red] [bold cyan]当前输入命令错误，请重新输入.[/bold cyan]")

    # ----------------------------------------分割----------------------------------------
    # 退出不报错
    def do_EOF(self, line):
        return True
        pass

    # ----------------------------------------分割----------------------------------------
    # 清空
    def do_clear(self, arg):
        '''清空屏幕'''
        clear()

    
    # ----------------------------------------分割----------------------------------------
    # 退出
    def do_exit(self, arg):
        '''退出工具'''
        sys.exit(1)

    def __init__(self):
        super().__init__()
        self.hidden_commands.append('EOF')
        self.hidden_commands.append('alias')
        self.hidden_commands.append('edit')
        self.hidden_commands.append('quit')
        self.hidden_commands.append('history')
        self.hidden_commands.append('macro')
        self.hidden_commands.append('run_pyscript')
        self.hidden_commands.append('run_script')
        self.hidden_commands.append('set')
        self.hidden_commands.append('shell')
        self.hidden_commands.append('shortcuts')


if __name__ == '__main__':
    clear()
    newcmd().cmdloop()
