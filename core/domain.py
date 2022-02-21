import os
import yaml
import json
import time
import random
import base64
import requests
import datetime as d
import core.api as api
from rich.progress import track
from rich.console import Console
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

sleeptime=random.randint(0, 2)

with open('config/config.yaml','r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.CLoader)

console = Console()

def domainscan(domain):
    if config['systeam'] == 'mac':
        Domain = []
        file = open('%s/domain.txt'%(config['Output']), mode='w')
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]FOFA[/bold green] > [bold purple]正在启动FOFA探测节点进行子域名探测...[/bold purple]")
        api.fofa_info()
        time.sleep(sleeptime)
        domain1 = 'domain="' + domain + '"'
        key = str(base64.b64encode(domain1.encode("utf-8")), "utf-8")
        url = "https://fofa.info/api/v1/search/all?email=%s&key=%s&qbase64=%s&size=%s&full=%s&fields=host"%(config['fofa_email'], config['fofa_Key'], key, config['fofa_limits'], config['Full'])
        r =requests.get(url, verify=False)
        json_data = json.loads(r.text)
        for i in range(0,int(len(json_data['results']))):
            Domain.append(json_data['results'][i])
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动Quake探测节点ing.........[/bold yellow]")
        time.sleep(2)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Quake[/bold green] > [bold purple]正在启动Quake探测节点进行子域名探测...[/bold purple]")
        api.quake_info()
        time.sleep(sleeptime)
        domain1 = 'domain:"' + domain + '"'
        url = "https://quake.360.cn/api/v3/search/quake_service"
        headers = {
        "X-QuakeToken": config['quake_key'],
        "Content-Type": "application/json"
        }   
        data = {
         "query": domain1,
         "start": 0,
         "size": config['quake_limits'],
         "ignore_cache": config['ignore_cache'],
         "latest": config['latest'],
         "include": ["service.http.host"],
         "start_time": config['start_time']
        }   
        r = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
        response = json.loads(r.text)
        for i in range(0,int(len(response['data']))):
            data = response['data'][i]
            Domain.append(data['service']['http']['host'])
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动ksubdomain枚举节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Ksubdomain[/bold green] > [bold purple]正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...[/bold purple]")
        os.system("./core/plus/mac/ksubdomain enum --band 1G --domain %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(domain, config["level"], config['Output'] + '/' + date + "_domain.txt"))
        with open(config['Output'] + '/' + date + "_domain.txt",'r') as f:
            for line in f:
                lst1 = f.read().splitlines()
        for i in lst1:
            if i not in Domain:
                Domain.append(i)
        for i in Domain:
            file.write('%s\n'%(i))
        file.close()
        os.remove(config['Output'] + '/' + date + "_domain.txt")
        os.remove("./ksubdomain.yaml")
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动Httpx验证节点ing.........[/bold yellow]")
        time.sleep(2)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Httpx[/bold green] > [bold purple]正在启动Httpx验证节点进行子域名验证...[/bold purple]")
        os.system("./core/plus/mac/httpx -l %s -content-length -title -tech-detect -status-code -threads 200 -silent"%(config['Output'] + "/domain.txt"))
    elif config['systeam'] == 'windows':
        Domain = []
        file = open('%s\\domain.txt'%(config['Output']), mode='w')
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]FOFA[/bold green] > [bold purple]正在启动FOFA节点进行子域名探测...[/bold purple]")
        api.fofa_info()
        time.sleep(sleeptime)
        domain1 = 'domain="' + domain + '"'
        key = str(base64.b64encode(domain1.encode("utf-8")), "utf-8")
        url = "https://fofa.info/api/v1/search/all?email=%s&key=%s&qbase64=%s&size=%s&full=%s&fields=host"%(config['fofa_email'], config['fofa_Key'], key, config['fofa_limits'], config['Full'])
        r =requests.get(url, verify=False)
        json_data = json.loads(r.text)
        for i in range(0,int(len(json_data['results']))):
            Domain.append(json_data['results'][i])
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动Quake节点ing.........[/bold yellow]")
        time.sleep(2)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Quake[/bold green] > [bold purple]正在启动Quake节点进行子域名探测...[/bold purple]")
        api.quake_info()
        time.sleep(sleeptime)
        domain1 = 'domain:"' + domain + '"'
        url = "https://quake.360.cn/api/v3/search/quake_service"
        headers = {
        "X-QuakeToken": config['quake_key'],
        "Content-Type": "application/json"
        }   
        data = {
         "query": domain1,
         "start": 0,
         "size": config['quake_limits'],
         "ignore_cache": config['ignore_cache'],
         "latest": config['latest'],
         "include": ["service.http.host"],
         "start_time": config['start_time']
        }   
        r = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
        response = json.loads(r.text)
        for i in range(0,int(len(response['data']))):
            data = response['data'][i]
            Domain.append(data['service']['http']['host'])
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动ksubdomain节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Ksubdomain[/bold green] > [bold purple]正在启动ksubdomain节点进行子域名枚举...[/bold purple]")
        os.system("core\\plus\\windows\\ksubdomain.exe enum --domain %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(domain, config["level"], config['Output'] + '\\' + date + "_domain.txt"))
        with open(config['Output'] + '\\' + date + "_domain.txt",'r') as f:
            for line in f:
                lst1 = f.read().splitlines()
        for i in lst1:
            if i not in Domain:
                Domain.append(i)
        for i in Domain:
            file.write('%s\n'%(i))
        file.close()
        os.remove(config['Output'] + '/' + date + "_domain.txt")
        os.remove("./ksubdomain.yaml")
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动Httpx验证节点ing.........[/bold yellow]")
        time.sleep(2)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Httpx[/bold green] > [bold purple]正在启动Httpx验证节点进行子域名验证...[/bold purple]")
        os.system("core\\plus\\windows\\httpx.exe -l %s -content-length -title -tech-detect -status-code -threads 200 -silent"%(config['Output'] + "\\domain.txt"))
    elif config['systeam'] == 'linux':
        Domain = []
        file = open('%s/domain.txt'%(config['Output']), mode='w')
        date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]FOFA[/bold green] > [bold purple]正在启动FOFA节点进行子域名探测...[/bold purple]")
        api.fofa_info()
        time.sleep(sleeptime)
        domain1 = 'domain="' + domain + '"'
        key = str(base64.b64encode(domain1.encode("utf-8")), "utf-8")
        url = "https://fofa.info/api/v1/search/all?email=%s&key=%s&qbase64=%s&size=%s&full=%s&fields=host"%(config['fofa_email'], config['fofa_Key'], key, config['fofa_limits'], config['Full'])
        r =requests.get(url, verify=False)
        json_data = json.loads(r.text)
        for i in range(0,int(len(json_data['results']))):
            Domain.append(json_data['results'][i])
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动Quake节点ing.........[/bold yellow]")
        time.sleep(2)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Quake[/bold green] > [bold purple]正在启动Quake节点进行子域名探测...[/bold purple]")
        api.quake_info()
        time.sleep(sleeptime)
        domain1 = 'domain:"' + domain + '"'
        url = "https://quake.360.cn/api/v3/search/quake_service"
        headers = {
        "X-QuakeToken": config['quake_key'],
        "Content-Type": "application/json"
        }   
        data = {
         "query": domain1,
         "start": 0,
         "size": config['quake_limits'],
         "ignore_cache": config['ignore_cache'],
         "latest": config['latest'],
         "include": ["service.http.host"],
         "start_time": config['start_time']
        }   
        r = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
        response = json.loads(r.text)
        for i in range(0,int(len(response['data']))):
            data = response['data'][i]
            Domain.append(data['service']['http']['host'])
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动ksubdomain节点ing.........[/bold yellow]")
        time.sleep(3)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Ksubdomain[/bold green] > [bold purple]正在启动ksubdomain节点进行子域名枚举...[/bold purple]")
        os.system("./core/plus/linux/ksubdomain enum --domain %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(domain, config["level"], config['Output'] + '/' + date + "_domain.txt"))
        with open(config['Output'] + '/' + date + "_domain.txt",'r') as f:
            for line in f:
                lst1 = f.read().splitlines()
        for i in lst1:
            if i not in Domain:
                Domain.append(i)
        for i in Domain:
            file.write('%s\n'%(i))
        file.close()
        os.remove(config['Output'] + '/' + date + "_domain.txt")
        os.remove("./ksubdomain.yaml")
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold red]Log[/bold red] > [bold yellow]扫描结束 正在启动Httpx验证节点ing.........[/bold yellow]")
        time.sleep(2)
        console.print("[[bold red]"+ str(base64.b64decode("V2FuTGkgU2Nhbg=="), "utf-8") +"[/bold red]] [[bold green]+[/bold green]] [bold green]Httpx[/bold green] > [bold purple]正在启动Httpx验证节点进行子域名验证...[/bold purple]")
        os.system("./core/plus/linux/httpx -l %s -content-length -title -tech-detect -status-code -threads 200 -silent"%(config['Output'] + "/domain.txt"))
