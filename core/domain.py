import os
import sys
import csv
import yaml
import json
import time
import random
import base64
import requests
import datetime as d
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import core.api as api
import core.lib as lib
from rich.progress import track
from rich.console import Console
from rich.table import Column, Table
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

sleeptime=random.randint(0, 2)

console = Console()

with open('config/config.yaml','r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.CLoader)

def domainscan(args,domain):
    if config['system'] == 'mac':
        if config['verify'] == True:
            Domain = []
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            lib.info('正在启动FOFA探测节点进行子域名探测...')
            time.sleep(sleeptime)
            api.fofa_domain(domain, Domain)
            lib.info('正在启动Quake探测节点进行子域名探测...')
            time.sleep(sleeptime)
            api.quake_domain(domain,Domain)
            file = open('logs/domain.txt', mode='w', encoding="utf-8")
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            time.sleep(sleeptime)
            os.system("./core/plus/mac/ksubdomain enum --band 1G -%s %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(args, domain, config["level"], 'logs/domain.txt'))
            os.remove("./ksubdomain.yaml")
            with open('logs/domain.txt', 'r', encoding="utf-8") as f:
                for line in f:
                    lst1 = f.read().splitlines()
            for i in lst1:
                if i not in Domain:
                    Domain.append(i)
            for i in Domain:
                print(i)
                file.write('%s\n'%(i))
            file.close()
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            time.sleep(sleeptime)
            os.system("./core/plus/mac/httpx -l logs/domain.txt -cdn -ec -content-length -title -tech-detect -status-code -threads 200 -silent -csv -o %s/domain.csv"%(config["Output"]))
            lib.clear()
            lib.info('正在启动FOFA探测节点进行子域名探测...')
            lib.info('正在启动Quake探测节点进行子域名探测...')
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            table = Table(show_header=True)
            table.add_column("ID", style="dim")
            table.add_column("IP")
            table.add_column('CDN')
            table.add_column("Url")
            table.add_column("Port")
            table.add_column("Title")
            table.add_column("Code")
            table.add_column("Length")
            table.add_column("Technologies")
            csv_reader = csv.reader(open("%s/domain.csv"%(config["Output"]), encoding="utf-8"))
            ii = 0
            Output = open('%s/domain.txt'%(config['Output']), mode='w', encoding="utf-8")
            for line in csv_reader:
                Url = line[10]
                if 'http' in Url:
                    ID = ii
                    IP = line[19]
                    Port = line[4]
                    Url = line[10]
                    Title = line[13]
                    Length = line[20]
                    Code = line[22]
                    CDN = line[29]
                    Technologies = line[31]
                    Output.write('%s\n'%(Url))
                    table.add_row(
                        str(ii),
                        str(IP),
                        str(CDN),
                        str(Url),
                        str(Port),
                        str(Title),
                        str(Code),
                        str(Length),
                        str(Technologies.strip('[').strip(']'))
                        )
                    ii += 1
                else:
                    continue
            Output.close()
            console.print(table)
            lib.info('The result file is saved at：' + config['Output'] + '/domain.csv')
        else:
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            os.system("./core/plus/mac/ksubdomain enum --band 1G -%s %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(args, domain, config["level"], 'logs/domain.txt'))
            os.remove("./ksubdomain.yaml")
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            os.system("./core/plus/mac/httpx -l %s -content-length -title -tech-detect -status-code -threads 200 -silent -csv -o %s/domain.csv"%('logs/domain.txt',config["Output"]))
            lib.clear()
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            table = Table(show_header=True)
            table.add_column("ID", style="dim")
            table.add_column("IP")
            table.add_column('CDN')
            table.add_column("Url")
            table.add_column("Port")
            table.add_column("Title")
            table.add_column("Code")
            table.add_column("Length")
            table.add_column("Technologies")
            csv_reader = csv.reader(open("%s/domain.csv"%(config["Output"]), encoding='utf-8'))
            ii = 0
            Output = open('%s/domain.txt'%(config['Output']), mode='w', encoding="utf-8")
            for line in csv_reader:
                Url = line[10]
                if 'http' in Url:
                    ID = ii
                    IP = line[19]
                    Port = line[4]
                    Url = line[10]
                    Title = line[13]
                    Length = line[20]
                    Code = line[22]
                    CDN = line[29]
                    Technologies = line[31]
                    Output.write('%s\n'%(Url))
                    table.add_row(
                        str(ii),
                        str(IP),
                        str(CDN),
                        str(Url),
                        str(Port),
                        str(Title),
                        str(Code),
                        str(Length),
                        str(Technologies.strip('[').strip(']'))
                        )
                    ii += 1
                else:
                    continue
            Output.close()
            console.print(table)
            lib.info('The result file is saved at：' + config['Output'] + '/domain.csv')
    elif config['system'] == 'linux':
        if config['verify'] == True:
            Domain = []
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            lib.info('正在启动FOFA探测节点进行子域名探测...')
            time.sleep(sleeptime)
            api.fofa_domain(domain, Domain)
            lib.info('正在启动Quake探测节点进行子域名探测...')
            time.sleep(sleeptime)
            api.quake_domain(domain,Domain)
            file = open('logs/domain.txt', mode='w', encoding="utf-8")
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            time.sleep(sleeptime)
            os.system("./core/plus/linux/ksubdomain enum --band 1G -%s %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(args, domain, config["level"], 'logs/domain.txt'))
            os.remove("./ksubdomain.yaml")
            with open('logs/domain.txt', 'r', encoding="utf-8") as f:
                for line in f:
                    lst1 = f.read().splitlines()
            for i in lst1:
                if i not in Domain:
                    Domain.append(i)
            for i in Domain:
                print(i)
                file.write('%s\n'%(i))
            file.close()
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            time.sleep(sleeptime)
            os.system("./core/plus/linux/httpx -l logs/domain.txt -cdn -content-length -title -tech-detect -status-code -threads 200 -silent -csv -o %s/domain.csv"%(config["Output"]))
            lib.clear()
            lib.info('正在启动FOFA探测节点进行子域名探测...')
            lib.info('正在启动Quake探测节点进行子域名探测...')
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            table = Table(show_header=True)
            table.add_column("ID", style="dim")
            table.add_column("IP")
            table.add_column('CDN')
            table.add_column("Url")
            table.add_column("Port")
            table.add_column("Title")
            table.add_column("Code")
            table.add_column("Length")
            table.add_column("Technologies")
            csv_reader = csv.reader(open("%s/domain.csv"%(config["Output"]), encoding="utf-8"))
            ii = 0
            Output = open('%s/domain.txt'%(config['Output']), mode='w', encoding="utf-8")
            for line in csv_reader:
                Url = line[10]
                if 'http' in Url:
                    ID = ii
                    IP = line[19]
                    Port = line[4]
                    Url = line[10]
                    Title = line[13]
                    Length = line[20]
                    Code = line[22]
                    CDN = line[29]
                    Technologies = line[31]
                    Output.write('%s\n'%(Url))
                    table.add_row(
                        str(ii),
                        str(IP),
                        str(CDN),
                        str(Url),
                        str(Port),
                        str(Title),
                        str(Code),
                        str(Length),
                        str(Technologies.strip('[').strip(']'))
                        )
                    ii += 1
                else:
                    continue
            Output.close()
            console.print(table)
            lib.info('The result file is saved at：' + config['Output'] + '/domain.csv')
        else:
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            os.system("./core/plus/linux/ksubdomain enum --band 1G -%s %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(args, domain, config["level"], 'logs/domain.txt'))
            os.remove("./ksubdomain.yaml")
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            os.system("./core/plus/linux/httpx -l logs/domain.txt -content-length -title -tech-detect -status-code -threads 200 -silent -csv -o %s/domain.csv"%(config["Output"]))
            lib.clear()
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            table = Table(show_header=True)
            table.add_column("ID", style="dim")
            table.add_column("IP")
            table.add_column('CDN')
            table.add_column("Url")
            table.add_column("Port")
            table.add_column("Title")
            table.add_column("Code")
            table.add_column("Length")
            table.add_column("Technologies")
            csv_reader = csv.reader(open("%s/domain.csv"%(config["Output"]), encoding='utf-8'))
            ii = 0
            Output = open('%s/domain.txt'%(config['Output']), mode='w', encoding="utf-8")
            for line in csv_reader:
                Url = line[10]
                if 'http' in Url:
                    ID = ii
                    IP = line[19]
                    Port = line[4]
                    Url = line[10]
                    Title = line[13]
                    Length = line[20]
                    Code = line[22]
                    CDN = line[29]
                    Technologies = line[31]
                    Output.write('%s\n'%(Url))
                    table.add_row(
                        str(ii),
                        str(IP),
                        str(CDN),
                        str(Url),
                        str(Port),
                        str(Title),
                        str(Code),
                        str(Length),
                        str(Technologies.strip('[').strip(']'))
                        )
                    ii += 1
                else:
                    continue
            Output.close()
            console.print(table)
            lib.info('The result file is saved at：' + config['Output'] + '/domain.csv')
    if config['system'] == 'windows':
        if config['verify'] == True:
            Domain = []
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            lib.info('正在启动FOFA探测节点进行子域名探测...')
            time.sleep(sleeptime)
            api.fofa_domain(domain, Domain)
            lib.info('正在启动Quake探测节点进行子域名探测...')
            time.sleep(sleeptime)
            api.quake_domain(domain,Domain)
            file = open('%s\\domain.txt'%(config['Output']), mode='w', encoding="utf-8")
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            time.sleep(sleeptime)
            os.system("core\\plus\\windows\\ksubdomain.exe enum --band 1G -%s %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(args, domain, config["level"], 'logs/domain.txt'))
            os.remove("ksubdomain.yaml")
            with open('logs/domain.txt', 'r', encoding="utf-8") as f:
                for line in f:
                    lst1 = f.read().splitlines()
            for i in lst1:
                if i not in Domain:
                    Domain.append(i)
            for i in Domain:
                print(i)
                file.write('%s\n'%(i))
            file.close()
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            time.sleep(sleeptime)
            os.system("core\\plus\\windows\\httpx.exe -l logs/domain.txt -cdn -content-length -title -tech-detect -status-code -threads 200 -silent -csv -o %s\\domain.csv"%(config["Output"]))
            lib.clear()
            lib.info('正在启动FOFA探测节点进行子域名探测...')
            lib.info('正在启动Quake探测节点进行子域名探测...')
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            table = Table(show_header=True)
            table.add_column("ID", style="dim")
            table.add_column("IP")
            table.add_column('CDN')
            table.add_column("Url")
            table.add_column("Port")
            table.add_column("Title")
            table.add_column("Code")
            table.add_column("Length")
            table.add_column("Technologies")
            csv_reader = csv.reader(open("%s\\domain.csv"%(config["Output"]), encoding="utf-8"))
            ii = 0
            Output = open('%s/domain.txt'%(config['Output']), mode='w', encoding="utf-8")
            for line in csv_reader:
                Url = line[10]
                if 'http' in Url:
                    ID = ii
                    IP = line[19]
                    Port = line[4]
                    Url = line[10]
                    Title = line[13]
                    Length = line[20]
                    Code = line[22]
                    CDN = line[29]
                    Technologies = line[31]
                    Output.write('%s\n'%(Url))
                    table.add_row(
                        str(ii),
                        str(IP),
                        str(CDN),
                        str(Url),
                        str(Port),
                        str(Title),
                        str(Code),
                        str(Length),
                        str(Technologies.strip('[').strip(']'))
                        )
                    ii += 1
                else:
                    continue
            Output.close()
            console.print(table)
            lib.info('The result file is saved at：' + config['Output'] + '/domain.csv')
        else:
            date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            os.system("core\\plus\\windows\\ksubdomain.exe enum --band 1G -%s %s --skip-wild --silent --only-domain --level %s --retry 1 --output %s"%(args, domain, config["level"], 'logs/domain.txt'))
            os.remove("./ksubdomain.yaml")
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            os.system("core\\plus\\windows\\httpx.exe -l logs/domain.txt -content-length -title -tech-detect -status-code -threads 200 -silent -csv -o %s\\domain.csv"%(config["Output"]))
            lib.clear()
            lib.info('正在启动ksubdomain枚举节点进行子域名枚, 预计用时过长请耐心等待...')
            lib.info('正在启动Httpx验证节点进行子域名验证...')
            table = Table(show_header=True)
            table.add_column("ID", style="dim")
            table.add_column("IP")
            table.add_column('CDN')
            table.add_column("Url")
            table.add_column("Port")
            table.add_column("Title")
            table.add_column("Code")
            table.add_column("Length")
            table.add_column("Technologies")
            csv_reader = csv.reader(open("%s\\domain.csv"%(config["Output"]), encoding='utf-8'))
            ii = 0
            Output = open('%s/domain.txt'%(config['Output']), mode='w', encoding="utf-8")
            for line in csv_reader:
                Url = line[10]
                if 'http' in Url:
                    ID = ii
                    IP = line[19]
                    Port = line[4]
                    Url = line[10]
                    Title = line[13]
                    Length = line[20]
                    Code = line[22]
                    CDN = line[29]
                    Technologies = line[31]
                    Output.write('%s\n'%(Url))
                    table.add_row(
                        str(ii),
                        str(IP),
                        str(CDN),
                        str(Url),
                        str(Port),
                        str(Title),
                        str(Code),
                        str(Length),
                        str(Technologies.strip('[').strip(']'))
                        )
                    ii += 1
                else:
                    continue
            Output.close()
            console.print(table)
            lib.info('The result file is saved at：' + config['Output'] + '/domain.csv')

# def path(args, domain, path):
#     lib.info('正在启动Httpx验证节点进行资产验证...')
#     time.sleep(sleeptime)
#     os.system("./core/plus/mac/httpx %s %s -path %s -mc %s -cdn -ec -content-length -title -tech-detect -status-code -threads 500 -silent -csv -o %s/Path.csv"%(args,domain, path, config["mc"], config["Output"]))
#     table = Table(show_header=True)
#     table.add_column("ID", style="dim")
#     table.add_column("IP")
#     table.add_column('CDN')
#     table.add_column("Url")
#     table.add_column("Port")
#     table.add_column("Title")
#     table.add_column("Code")
#     table.add_column("Length")
#     table.add_column("Technologies")
#     csv_reader = csv.reader(open("%s/Path.csv"%(config["Output"])))
#     ii = 0
#     Output = open('%s/Path.txt'%(config['Output']), mode='w', encoding="utf-8")
#     for line in csv_reader:
#         Url = line[10]
#         if 'http' in Url:
#             ID = ii
#             IP = line[19]
#             Port = line[4]
#             Url = line[10]
#             Title = line[13]
#             Length = line[20]
#             Code = line[22]
#             CDN = line[29]
#             Technologies = line[31]
#             Output.write('%s\n'%(Url))
#             table.add_row(
#                 str(ii),
#                 str(IP),
#                 str(CDN),
#                 str(Url),
#                 str(Port),
#                 str(Title),
#                 str(Code),
#                 str(Length),
#                 str(Technologies.strip('[').strip(']'))
#                 )
#             ii += 1
#         else:
#             continue
#     Output.close()
#     lib.clear()
#     lib.info('正在启动Httpx验证节点进行资产验证...')
#     console.print(table)