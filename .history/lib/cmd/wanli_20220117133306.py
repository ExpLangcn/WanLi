import getpass
import os
import sys
from turtle import st
import config.config
from os import system
from rich.table import Table
from datetime import datetime
from rich.console import Console

console = Console()

def dirscan(url):
    console.print("[bold green][+]即将扫描[bold cyan] " +url + " 的敏感文件及敏感地址[/bold cyan]")
    console.print("[bold green][+][/bold green] [bold cyan]正在准备扫描中...[/bold cyan]")
    datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    system(config.config.PYTHON + " " +config.config.dirsearch +r" -u " + url +r" -r -t 150 --recursion-status=200,301,302 --exclude-sizes=3KB -q --format json -o logs/" + datatime + r"_dirscan_output.json")

def domain(domain):
    console.print("[bold green][+]即将扫描[bold cyan] " +domain + "[/bold cyan] 的相关域名及子域名（[bold red]自动验证 用时过长 预计1-3分钟.[/bold red]）")
    console.print("[bold green][+][/bold green] [bold cyan]正在准备扫描中...[/bold cyan]")
    console.print("[bold green][+][/bold green] [bold cyan]格式：域名 [[bold red]状态码[/bold red]] [[bold red]Length[/bold red]] [[bold red]Title[/bold red]] [[bold red]中间件[/bold red]][/bold cyan]")
    datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    system(config.config.subfinder + r" -silent -recursive -t 200 -d " + domain +r" | " + config.config.ksubdomain + r" -verify -silent | "+ config.config.httpx +r" -content-length -title -tech-detect -status-code -threads 200 -silent -o logs/" + datatime + r"_domain_output.txt")

def ddir(domain):
    console.print("[bold green][+] 即将扫描[bold cyan] " + domain +"[/bold cyan] 的[bold red]相关域名[/bold red]及[bold red]子域名[/bold red]的[bold red]敏感文件[/bold red]及[bold red]敏感地址[/bold red]")
    console.print("[bold green][+][/bold green] [bold cyan]正在准备扫描中...[/bold cyan]")
    datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    system(config.config.subfinder + r" -silent -recursive -t 150 -d " + domain +r" | " + config.config.ksubdomain + r" -verify -silent | "+ config.config.httpx +r" -threads 150 -silent -o logs/" + datatime + r"_domain_output.txt && " + config.config.PYTHON + " " + config.config.dirsearch +r" -l " + r"logs/" + datatime + r"_domain_output.txt -r -t 150 --recursion-status=200,301,302 --exclude-sizes=3KB -q --format csv -o logs/" + datatime + r"_ddir_output.csv")

CVE_list = []

def search(path, keyword):
    content = os.listdir(path)
    for each in content:
        each_path = path + os.sep + each
        if keyword in each:
            CVE_list.append(each_path)
        if os.path.isdir(each_path):
            search(each_path, keyword)

def s_pocscan(keyword, table):
    search('./lib/POC', keyword)
    table.add_column('[red]Name')
    table.add_column('Path')
    for i in CVE_list:
        table.add_row(keyword, i)
    console.print(table)
    CVE_list.clear()

def u_pocscan(url, theme):
    console.print("[bold green][+][/bold green] [bold cyan]即将扫描 " + str(url) + " 的漏洞.")
    console.print("[bold green][+][/bold green] [bold cyan]正在准备扫描中...")
    datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    system(config.config.nuclei + r" -u " + str(url) + " -t '" + str(theme) + "' -silent -nts -o logs/pocscan_" + datatime + r"_ok.txt -me logs/pocscan" + datatime + r"_md/")

def l_pocscan(file, theme):
    f = open(file, "r", encoding="UTF-8") 
    for line in f.readlines():
        line = line.split()
        for i in line:
            console.print("[bold green][+][/bold green] [bold cyan]即将扫描 " + str(i) + " 的漏洞.")
            console.print("[bold green][+][/bold green] [bold cyan]正在准备扫描中...")
            datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            system(config.config.nuclei + r" -u " + str(i) + " -t '" + str(theme) + "' -silent -nts -o logs/pocscan_" + datatime + r"_ok.txt -me logs/pocscan_" + datatime + r"_md/")

def portscan(target):
    console.print("[bold green][+][/bold green] [bold cyan]即将扫描 " + str(target) + " 的端口,(全端口扫描 自动验证 速度略慢 平均2-5分钟.)")
    console.print("[bold green][+][/bold green] [bold cyan]正在准备扫描中...")
    datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    system(config.config.naabu + r" -p - -host " + str(target) + " -c 200 -verify -silent -o logs/portscan_" + datatime + r"_ok.txt")

def g_fofascan(target):
    if config.config.email == '':
        Email = console.input("Email：")
        Key = getpass.getpass("Key：")
        datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        system(config.config.fofa + r" -m " + str(Email) + r" -k " + str(Key) + r" -q " + r"'" + str(target) + r"'" + r" -o logs/FOFA_" + datatime + r"_" + str(target) +r".txt")
    else:
        datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        system(config.config.fofa + r" -q " + r"'" + str(target) + r"'" + r" -o logs/FOFA_" + datatime + r"_" + str(target) +r".txt")