from __future__ import print_function
from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
import base64
import argparse
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import core.vulscan as vulscan
import core.domain as domain
import core.lib as lib
import core.api as api
import yaml
import datetime as d
from rich.console import Console

console = Console()

style = Style.from_dict({
    # User input (default text).
    '':          '#00FF00 bold',

    # Prompt.
    'username': '#FFFFFF bold',
    'null':'#A9A9A9 bold',
    'fuhao':'#FFFFFF bold',
    'args': '#FF0000 bold',
})
lib.clear()
while True:
    message = [
    ('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")),
    ('class:null', ' > '),
]
    Completer = WordCompleter(['help', 'exit','clear', 'clear', 'scan', 'fofa','quake'], ignore_case=True)
    user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
    if user_input.strip().lower() == 'clear':
        lib.clear()
    if user_input.strip().lower() == 'help':
        console.print('''
Usage: scan.py [OPTIONS] COMMAND [ARGS]...

Options:
  help            Display help information.
  clear           clear.
  exit            Exit the WanLi Scan client.
  run  <target>   Run target.

Commands:
  fofa  Use FOFA for asset scanning and other functions.
  quake Use 360 Quake for asset scanning and other functions.
  scan  Security detection of target assets.''')
    if user_input.strip().lower() == 'scan':
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        message.clear()
        message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
        message.append(('class:fuhao', ' (', "utf-8"))
        message.append(('class:args', user_input.strip().lower()))
        message.append(('class:fuhao', ')', "utf-8"))
        message.append(('class:null', ' > '))
        Completer = WordCompleter(['help', 'exit','clear','pocscan', 'domain','ldomain','dscan'], ignore_case=True)
        user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
        if user_input.strip().lower() == 'clear':
            lib.clear()
        if user_input.strip().lower() == 'help':
            console.print('''
Usage: scan.py [OPTIONS] COMMAND [ARGS]...

Options:
  help            Display help information.
  clear           clear.
  exit            Exit the WanLi Scan client.
  run  <target>   Run target.

Commands:
  pocscan   Vulnerability detection of target files. (Url or domain name may exist in the file)
  domain    Subdomain probing for a single target.
  ldomain   Subdomain detection of target files.
  dscan     Automatically detect subdomains, and perform vulnerability scanning on subdomain detection results. (Only supports scanning a single subdomain)''')
        if user_input.strip().lower() == 'pocscan':
    
            message.clear()
            message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
            message.append(('class:fuhao', ' (', "utf-8"))
            message.append(('class:args', user_input.strip().lower()))
            message.append(('class:fuhao', ')', "utf-8"))
            message.append(('class:null', ' > '))
            Completer = WordCompleter(["run "], ignore_case=True)
            user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
            if 'run' in user_input.strip().lower():
                with open('config/config.yaml','r', encoding='utf-8') as f:
                    config = yaml.load(f, Loader=yaml.CLoader)
                a = user_input.strip().lower()
                vulscan.pocscan(a[4:],date)
        if user_input.strip().lower() == 'domain':
    
            message.clear()
            message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
            message.append(('class:fuhao', ' (', "utf-8"))
            message.append(('class:args', user_input.strip().lower()))
            message.append(('class:fuhao', ')', "utf-8"))
            message.append(('class:null', ' > '))
            Completer = WordCompleter(["run "], ignore_case=True)
            user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
            if 'run' in user_input.strip().lower():
                with open('config/config.yaml','r', encoding='utf-8') as f:
                    config = yaml.load(f, Loader=yaml.CLoader)
                a = user_input.strip().lower()
                domain.domainscan('-d',a[4:])
        if user_input.strip().lower() == 'ldomain':
    
            message.clear()
            message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
            message.append(('class:fuhao', ' (', "utf-8"))
            message.append(('class:args', user_input.strip().lower()))
            message.append(('class:fuhao', ')', "utf-8"))
            message.append(('class:null', ' > '))
            Completer = WordCompleter(["run "], ignore_case=True)
            user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
            if 'run' in user_input.strip().lower():
                with open('config/config.yaml','r', encoding='utf-8') as f:
                    config = yaml.load(f, Loader=yaml.CLoader)
                a = user_input.strip().lower()
                domain.domainscan('-dl',a[4:])
        if user_input.strip().lower() == 'dscan':
    
            message.clear()
            message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
            message.append(('class:fuhao', ' (', "utf-8"))
            message.append(('class:args', user_input.strip().lower()))
            message.append(('class:fuhao', ')', "utf-8"))
            message.append(('class:null', ' > '))
            Completer = WordCompleter(["run "], ignore_case=True)
            user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
            if 'run' in user_input.strip().lower():
                with open('config/config.yaml','r', encoding='utf-8') as f:
                    config = yaml.load(f, Loader=yaml.CLoader)
                a = user_input.strip().lower()
                domain.domainscan('-d',a[4:])
                vulscan.pocscan('%s/domain.txt'%(config['Output']),date)
                f.close()
    if user_input.strip().lower() == 'fofa':
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

        message.clear()
        message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
        message.append(('class:fuhao', ' (', "utf-8"))
        message.append(('class:args', user_input.strip().lower()))
        message.append(('class:fuhao', ')', "utf-8"))
        message.append(('class:null', ' > '))
        Completer = WordCompleter(['help', 'exit','clear', 'search', 'limits','sscan'], ignore_case=True)
        user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
        if user_input.strip().lower() == 'clear':
            lib.clear()
        if user_input.strip().lower() == 'help':
            console.print('''
Usage: scan.py [OPTIONS] COMMAND [ARGS]...

Options:
  help            Display help information.
  clear           clear.
  exit            Exit the WanLi Scan client.
  run  <target>   Run target.

Commands:
  search             Asset Scanning with FOFA.
  limits  <target>   Modify the number of FOFA searches.
  sscan   <target>   Automatic FOFA search for assets, and automatic vulnerability scanning after the end.''')
        if 'limits' in user_input.strip().lower():
            with open('config/config.yaml','r', encoding='utf-8') as f:
                config = yaml.load(f, Loader=yaml.CLoader)
            a = user_input.strip().lower()
            lib.alter("config/config.yaml", "fofa_limits : " + str(config['fofa_limits']), "fofa_limits : " + a[7:])
            f.close()
        if user_input.strip().lower() == 'search':
    
            message.clear()
            message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
            message.append(('class:fuhao', ' (', "utf-8"))
            message.append(('class:args', user_input.strip().lower()))
            message.append(('class:fuhao', ')', "utf-8"))
            message.append(('class:null', ' > '))
            Completer = WordCompleter(["run "], ignore_case=True)
            user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
            if 'run' in user_input.strip().lower():
                with open('config/config.yaml','r', encoding='utf-8') as f:
                    config = yaml.load(f, Loader=yaml.CLoader)
                a = user_input.strip().lower()
                api.fofa_search(a[4:], date)
        if 'sscan' in user_input.strip().lower():
            a = user_input.strip().lower()
            with open('config/config.yaml','r', encoding='utf-8') as f:
                config = yaml.load(f, Loader=yaml.CLoader)
            api.fofa_search(a[5:], date)
            vulscan.pocscan(config['Output'] + '/txt/' + date + "_keyword.txt",date)
            f.close()
    if user_input.strip().lower() == 'quake':
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

        message.clear()
        message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
        message.append(('class:fuhao', ' (', "utf-8"))
        message.append(('class:args', user_input.strip().lower()))
        message.append(('class:fuhao', ')', "utf-8"))
        message.append(('class:null', ' > '))
        Completer = WordCompleter(['help', 'exit','clear', 'search', 'limits','sscan'], ignore_case=True)
        user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
        if user_input.strip().lower() == 'clear':
            lib.clear()
        if user_input.strip().lower() == 'help':
            console.print('''
Usage: scan.py [OPTIONS] COMMAND [ARGS]...

Options:
  help            Display help information.
  clear           clear.
  exit            Exit the WanLi Scan client.
  run  <target>   Run target.

Commands:
  search            Asset Scanning with 360 Quake.
  limits <target>   Modify the number of 360 Quake searches.
  sscan  <target>   Automatic 360 Quake search for assets, and automatic vulnerability scanning after the end.''')
        if 'limits' in user_input.strip().lower():
            with open('config/config.yaml','r', encoding='utf-8') as f:
                config = yaml.load(f, Loader=yaml.CLoader)
            a = user_input.strip().lower()
            lib.alter("config/config.yaml", "quake_limits : " + str(config['quake_limits']), "quake_limits : " + a[7:])
            f.close()
        if user_input.strip().lower() == 'search':
    
            message.clear()
            message.append(('class:username', str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8")))
            message.append(('class:fuhao', ' (', "utf-8"))
            message.append(('class:args', user_input.strip().lower()))
            message.append(('class:fuhao', ')', "utf-8"))
            message.append(('class:null', ' > '))
            Completer = WordCompleter(["run "], ignore_case=True)
            user_input = prompt(message, style=style, auto_suggest=AutoSuggestFromHistory(), 
                        completer=Completer)
            if 'run' in user_input.strip().lower():
                a = user_input.strip().lower()
                api.quake_search(a[4:], date)
        if 'sscan' in user_input.strip().lower():
            with open('config/config.yaml','r', encoding='utf-8') as f:
                config = yaml.load(f, Loader=yaml.CLoader)
            a = user_input.strip().lower()
            api.quake_search(a[5:], date)
            vulscan.pocscan(config['Output'] + '/txt/' + date + "_keyword.txt",date)
            f.close()
    if user_input.strip().lower() == 'exit':
        break