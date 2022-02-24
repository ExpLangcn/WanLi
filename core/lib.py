import base64
import os
import sys
from rich.console import Console
from os import system, name
console = Console()

def error(title, body):
    console.print('''[[bold red]'''+ str(base64.b64decode('''V2FuTGkgU2Nhbg=='''), '''utf-8''') +'''[/bold red]] [[bold red]-[/bold red]] [bold red]'''+ title +'''[/bold red] > [bold yellow]'''+ body +'''[/bold yellow]''')
def correct(title, body):
    console.print('''[[bold red]'''+ str(base64.b64decode('''V2FuTGkgU2Nhbg=='''), '''utf-8''') +'''[/bold red]] [[bold green]+[/bold green]] [bold green]'''+ title +'''[/bold green] > [bold purple]'''+ body +'''[/bold purple]''')
def info(body):
    console.print('''[[bold red]'''+ str(base64.b64decode('''V2FuTGkgU2Nhbg=='''), '''utf-8''') +'''[/bold red]] [[bold green]+[/bold green]] [bold red]Info[/bold red] > '''+ body)
def alter(file,old_str,new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
def clear():
    if name == 'nt':
        _ = system('cls')
        console.print('''[bold bule]
         __          __         _      _    _____                 
         \ \        / /        | |    (_)  / ____|                
          \ \  /\  / /_ _ _ __ | |     _  | (___   ___ __ _ _ __  
           \ \/  \/ / _` | '_ \| |    | |  \___ \ / __/ _` | '_ \ 
            \  /\  / (_| | | | | |____| |  ____) | (_| (_| | | | |
             \/  \/ \__,_|_| |_|______|_| |_____/ \___\__,_|_| |_|

                    [bold magenta]GitHub:https://github.com/ExpLangcn[/bold magenta]  
          [[bold red]本工具仅供学习与参考，请勿用于非法用途！否则一切后果自负[/bold red]]  
                                                        Info：[bold green]ExpLang[/bold green]
                                                    作者微信：[bold green]backxyh[/bold green][/bold bule]
                                                    ''')
    else:
        _ = system('clear')
        console.print('''[bold bule]
         __          __         _      _    _____                 
         \ \        / /        | |    (_)  / ____|                
          \ \  /\  / /_ _ _ __ | |     _  | (___   ___ __ _ _ __  
           \ \/  \/ / _` | '_ \| |    | |  \___ \ / __/ _` | '_ \ 
            \  /\  / (_| | | | | |____| |  ____) | (_| (_| | | | |
             \/  \/ \__,_|_| |_|______|_| |_____/ \___\__,_|_| |_|

                    [bold magenta]GitHub:https://github.com/ExpLangcn[/bold magenta]  
          [[bold red]本工具仅供学习与参考，请勿用于非法用途！否则一切后果自负[/bold red]]  
                                                        Info：[bold green]ExpLang[/bold green]
                                                    作者微信：[bold green]backxyh[/bold green][/bold bule]
                                                    ''')