import base64
import os
import yaml
import time
import random
import datetime as d
import core.lib as core
from rich.console import Console
with open('config/config.yaml','r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.CLoader)
console = Console()
sleeptime=random.randint(0, 1)
def pocscan(domain,date):
    if config['system'] == 'mac':
        core.info('正在启动Nuclei漏扫节点ing...')
        time.sleep(3)
        update = console.input("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]VulScan[/bold green] >  [bold blue]是否进行漏洞库更新？Y or N：[bold blue]")
        if update == 'Y' or update =='y':
            core.correct('VulScan', '正在更新Nuclei漏洞库...')
            os.system("./core/plus/mac/nuclei -silent -ut -ud 'core/nuclei-templates'")
            core.correct('VulScan', '正在使用Nuclei漏扫节点进行漏洞扫描...')
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            os.system("./core/plus/mac/nuclei -l %s -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date +  "_pocscan.md"))
            core.info('The result file is saved at：' + config['Output'] + '/md/' + date +  "_pocscan.md")
        elif update == 'N' or update =='n':
            core.correct('VulScan', '正在使用Nuclei漏扫节点进行漏洞扫描...')
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            os.system("./core/plus/mac/nuclei -l %s -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date +  "_pocscan.md"))
            core.info('The result file is saved at：' + config['Output'] + '/md/' + date +  "_pocscan.md")
    if config['system'] == 'windows':
        core.info('正在启动Nuclei漏扫节点ing...')
        time.sleep(3)
        update = console.input("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]VulScan[/bold green] >  [bold blue]是否进行漏洞库更新？Y or N：[bold blue]")
        if update == 'Y' or update =='y':
            core.correct('VulScan', '正在更新Nuclei漏洞库...')
            os.system("core\\plus\\windows\\nuclei.exe -silent -ut -ud core\\nuclei-templates")
            core.correct('VulScan', '正在使用Nuclei漏扫节点进行漏洞扫描...')
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            os.system("core\\plus\\windows\\nuclei.exe -l %s -t core\\nuclei-templates\\ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '\\md\\' + date + "_pocscan.md"))
            core.info('The result file is saved at：' + config['Output'] + '/md/' + date +  "_pocscan.md")
        elif update == 'N' or update =='n':
            core.correct('VulScan', '正在使用Nuclei漏扫节点进行漏洞扫描...')
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            os.system("core\\plus\\windows\\nuclei.exe -l %s -t core\\nuclei-templates\\ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '\\md\\' + date + "_pocscan.md"))
            core.info('The result file is saved at：' + config['Output'] + '/md/' + date +  "_pocscan.md")
    if config['system'] == 'linux':
        core.info('正在启动Nuclei漏扫节点ing...')
        time.sleep(3)
        update = console.input("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]VulScan[/bold green] >  [bold blue]是否进行漏洞库更新？Y or N：[bold blue]")
        if update == 'Y' or update =='y':
            core.correct('VulScan', '正在更新Nuclei漏洞库...')
            os.system("./core/plus/linux/nuclei -silent -ut -ud 'core/nuclei-templates'")
            core.correct('VulScan', '正在使用Nuclei漏扫节点进行漏洞扫描...')
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            os.system("./core/plus/linux/nuclei -l %s -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date + "_pocscan.md"))
            core.info('The result file is saved at：' + config['Output'] + '/md/' + date +  "_pocscan.md")
        elif update == 'N' or update =='n':
            core.correct('VulScan', '正在使用Nuclei漏扫节点进行漏洞扫描...')
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            os.system("./core/plus/linux/nuclei -l %s -t ./core/nuclei-templates/ -s %s -silent -stats -si 10 -retries 2 -me %s"%(domain, config['severity'], config['Output'] + '/md/' + date + "_pocscan.md"))
            core.info('The result file is saved at：' + config['Output'] + '/md/' + date +  "_pocscan.md")