import base64
import os
import yaml
import time
import random
import datetime as d
from rich.console import Console

date=str(d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"))

with open('config/config.yaml','r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.CLoader)
console = Console()
sleeptime=random.randint(0, 1)
def pocscan(domain):
    if config['systeam'] == 'mac':
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在启动Nuclei漏扫节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在进行Nuclei漏扫库更新ing.........[/bold yellow]")
        os.system("./core/plus/mac/nuclei -silent -ut -ud 'core/nuclei-templates'")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Nuclei[/bold green] >  [bold purple]正在使用Nuclei漏扫节点进行漏洞扫描...[/bold purple]")
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        os.system("./core/plus/mac/nuclei -u %s -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date + "_pocscan.md"))
    if config['systeam'] == 'windows':
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在启动Nuclei漏扫节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在进行Nuclei漏扫库更新ing.........[/bold yellow]")
        os.system("./core/plus/mac/nuclei -silent -ut -ud 'core/nuclei-templates'")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Nuclei[/bold green] >  [bold purple]正在使用Nuclei漏扫节点进行漏洞扫描...[/bold purple]")
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        os.system("core\\plus\\windows\\nuclei.exe -u %s -t core\\nuclei-templates\\ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date + "_pocscan.md"))
    if config['systeam'] == 'linux':
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在启动Nuclei漏扫节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在进行Nuclei漏扫库更新ing.........[/bold yellow]")
        os.system("./core/plus/mac/nuclei -silent -ut -ud 'core/nuclei-templates'")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Nuclei[/bold green] >  [bold purple]正在使用Nuclei漏扫节点进行漏洞扫描...[/bold purple]")
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        os.system("./core/plus/linux/nuclei -u %s -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date + "_pocscan.md"))

def lscan(domain):
    if config['systeam'] == 'mac':
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在启动Nuclei漏扫节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在进行Nuclei漏扫库更新ing.........[/bold yellow]")
        os.system("./core/plus/mac/nuclei -silent -ut -ud 'core/nuclei-templates'")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Nuclei[/bold green] >  [bold purple]正在使用Nuclei漏扫节点进行漏洞扫描...[/bold purple]")
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        os.system("./core/plus/mac/nuclei -l '%s' -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date + "_pocscan.md"))
    if config['systeam'] == 'windows':
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在启动Nuclei漏扫节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在进行Nuclei漏扫库更新ing.........[/bold yellow]")
        os.system("./core/plus/mac/nuclei -silent -ut -ud 'core/nuclei-templates'")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Nuclei[/bold green] >  [bold purple]正在使用Nuclei漏扫节点进行漏洞扫描...[/bold purple]")
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        os.system("core\\plus\\windows\\nuclei.exe -l '%s' -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date + "_pocscan.md"))
    if config['systeam'] == 'linux':
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在启动Nuclei漏扫节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] >  [bold yellow]正在进行Nuclei漏扫库更新ing.........[/bold yellow]")
        os.system("./core/plus/mac/nuclei -silent -ut -ud 'core/nuclei-templates'")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Nuclei[/bold green] >  [bold purple]正在使用Nuclei漏扫节点进行漏洞扫描...[/bold purple]")
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        os.system("./core/plus/linux/nuclei -l '%s' -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date + "_pocscan.md"))