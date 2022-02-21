import yaml
import argparse
import core.vulscan as vulscan
import core.domain as domain
import core.api as api
import datetime as d
import time
from os import system, name
from rich.console import Console

with open('config/config.yaml','r') as f:
    config = yaml.load(f, Loader=yaml.CLoader)
console = Console()
   
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

                    [bold blue]GitHub:https://github.com/ExpLangcn[/bold blue]
           [[bold red]本工具仅供学习与参考，请勿用于非法用途！否则一切后果自负[/bold red]]

                                                    [bold green]--Info:ExpLang[/bold green]                                                                    
        [/bold bule]''')
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
                                                    [bold green]--Info:ExpLang[/bold green]                                                                    
        [/bold bule]''')
def alter(file,old_str,new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

parser = argparse.ArgumentParser()
parser.add_argument('-fofa', help='\033[1;32m使用 FOFA 进行关键字搜索\033[0m / \033[1;33mKeyword search using FOFA.\033[0m')
parser.add_argument('-fl', help='\033[1;32m修改 FOFA 的 Limits 配置\033[0m / \033[1;33mModify the Limits configuration of FOFA.\033[0m')

parser.add_argument('-quake', help='\033[1;32m使用 Quake 进行关键字搜索\033[0m / \033[1;33mKeyword search using Quake.\033[0m')
parser.add_argument('-ql', help='\033[1;32m修改 Quake 的 Limits 配置\033[0m / \033[1;33mModify the Limits configuration of Quake.\033[0m')

parser.add_argument('-domain', help='\033[1;32m使用 FOFA、Quake、ksubdomain 进行全面的子域检测\033[0m / \033[1;33mComprehensive subdomain detection using FOFA, Quake, ksubdomain.\033[0m')
parser.add_argument('-scan', action='store_true', help='\033[1;32m使用Nuclei对结果进行全部漏洞扫描漏洞检测\033[0m / \033[1;33mVulnerability Scanning All Vulnerability Detection on Targets Using Nuclei.\033[0m')
parser.add_argument('-poc', help='\033[1;32m使用Nuclei对目标进行全部漏洞扫描漏洞检测\033[0m / \033[1;33mVulnerability Scanning All Vulnerability Detection on Targets Using Nuclei.\033[0m')
parser.add_argument('-lscan', help='\033[1;32m使用Nuclei对文件内的目标进行全部漏洞扫描漏洞检测\033[0m / \033[1;33mVulnerability Scanning All Vulnerability Detection for Targets in Files Using Nuclei.\033[0m')

args = parser.parse_args()
if args.fofa and args.scan:
    clear()
    api.fofa_info()
    date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    api.fofa_search(args.fofa, date)
    time.sleep(1)
    vulscan.lscan(config['Output'] + '/txt/' + date + "_keyword.txt")
elif args.fofa:
    clear()
    api.fofa_info()
    date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    api.fofa_search(args.fofa, date)
if args.fl:
    alter("config/config.yaml", "fofa_limits : " + str(config['fofa_limits']), "fofa_limits : " + str(args.fl))

if args.quake and args.scan:
    clear()
    api.quake_info()
    date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    api.quake_search(args.quake, date)
    vulscan.lscan(config['Output'] + '/txt/' + date + "_keyword.txt")
elif args.quake:
    clear()
    api.quake_info()
    date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    api.quake_search(args.quake, date)
if args.ql:
    alter("config/config.yaml", "quake_limits : " + str(config['quake_limits']), "quake_limits : " + str(args.ql))

if args.domain and args.scan:
    clear()
    domain.domainscan(args.domain)
    time.sleep(1)
    vulscan.lscan(config['Output'] + '/' + "domain.txt")
elif args.domain:
    clear()
    domain.domainscan(args.domain)

if args.poc:
    clear()
    vulscan.pocscan(args.poc)
if args.lscan:
    clear()
    vulscan.lscan(args.lscan)