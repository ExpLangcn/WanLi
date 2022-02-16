import yaml
import argparse
import core.vulscan as vulscan
import core.domain as domain
import core.api as api
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

                    [bold magenta]GitHub:https://github.com/ExpLangcn[/bold magenta]    
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
parser.add_argument('-fdomain', help='\033[1;32m使用 FOFA 进行子域检测\033[0m / \033[1;33mSubdomain Detection Using FOFA.\033[0m')
parser.add_argument('-fl', help='\033[1;32m修改 FOFA 的 Limits 配置\033[0m / \033[1;33mModify the Limits configuration of FOFA.\033[0m')

parser.add_argument('-quake', help='\033[1;32m使用 Quake 进行关键字搜索\033[0m / \033[1;33mKeyword search using Quake.\033[0m')
parser.add_argument('-qdomain', help='\033[1;32m使用 Quake 进行子域检测\033[0m / \033[1;33mSubdomain Detection Using Quake.\033[0m')
parser.add_argument('-ql', help='\033[1;32m修改 Quake 的 Limits 配置\033[0m / \033[1;33mModify the Limits configuration of Quake.\033[0m')

parser.add_argument('-domain', help='\033[1;32m使用 FOFA、Quake、ksubdomain 进行全面的子域检测\033[0m / \033[1;33mComprehensive subdomain detection using FOFA, Quake, ksubdomain.\033[0m')
parser.add_argument('-pocscan', help='\033[1;32m使用Nuclei对目标进行全部漏洞扫描漏洞检测\033[0m / \033[1;33mVulnerability Scanning All Vulnerability Detection on Targets Using Nuclei.\033[0m')
parser.add_argument('-lscan', help='\033[1;32m使用Nuclei对文件内的目标进行全部漏洞扫描漏洞检测\033[0m / \033[1;33mVulnerability Scanning All Vulnerability Detection for Targets in Files Using Nuclei.\033[0m')

args = parser.parse_args()

if args.fofa:
    clear()
    api.fofa_info()
    api.fofa_search(args.fofa)
if args.fdomain:
    clear()
    api.fofa_domain(args.fdomain)
if args.fl:
    alter("config/config.yaml", "fofa_limits : " + str(config['fofa_limits']), "fofa_limits : " + str(args.fl))
if args.quake:
    clear()
    api.quake_info()
    api.quake_search(args.quake)
if args.qdomain:
    api.quake_domain(args.qdomain)
if args.ql:
    clear()
    alter("config/config.yaml", "quake_limits : " + str(config['quake_limits']), "quake_limits : " + str(args.ql))
if args.domain:
    clear()
    domain.domainscan(args.domain)
if args.pocscan:
    clear()
    vulscan.pocscan(args.pocscan)
if args.lscan:
    clear()
    vulscan.lscan(args.lscan)