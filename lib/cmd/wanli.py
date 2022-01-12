import os
import sys
import config.config
from os import system
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