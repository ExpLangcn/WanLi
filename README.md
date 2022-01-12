# WanLi

**[中文版](README_CN.md)** ｜[LICENSE](LICENSE) ｜ **[WanLi-ExpLang](https://twitter.com/ExpLang_Cn)**

Use Dirsearch, Subfinder, Ksubdomain, Httpx, nuclei tools to quickly check target assets and perform sensitive files, sensitive paths, and vulnerability verification detection on target assets.

* Directory scanning with Dirsearch
* Use Subfinder for subdomain detection
* Use Ksubdomain for domain name verification
* Use Httpx for domain name information detection
* Use nuclei for exploit and detection

# Performance

[![asciicast](https://asciinema.org/a/461330.svg)](https://asciinema.org/a/461330)

# Performance
```
git clone https://github.com/ExpLangcn/WanLi.git
cd WanLi & pip3 install -r requirements.txt
vim config/config.py
```

> Modify the corresponding path under Path, except the python path, you need to add "./"

![](img/16419804357030.jpg)
```
python3 WanLi.py
```
# Help
```
clear                 clear screen                                                                        
ddir                  Scan sensitive files and sensitive addresses of related domain names and subdomains of a single main domain name, ddir baidu.com            
dirscan               Scan a single web application for sensitive files and sensitive addresses, dirscan https://www.baidu.com/               
domain                Scan related domain names and subdomains of a single main domain name, domain baidu.com                              
exit                  Exit tool                                                                        
help                  List available commands or provide detailed help for a specific command         
pocscan               Scan single or multiple WEB application vulnerabilities, you can specify vulnerabilities or batch vulnerabilities, please use "*.yaml" for batch vulnerabilities
```

# Twitter

[@ExpLang_Cn](https://twitter.com/ExpLang_Cn)

# WeChat

![WechatIMG408](img/WechatIMG408.jpeg)

# Info

* **[ksubdomain](https://github.com/knownsec/ksubdomain)**

* **[dirsearch](https://github.com/maurosoria/dirsearch)**

* **[subfinder](https://github.com/projectdiscovery/subfinder)**

* **[httpx](https://github.com/projectdiscovery/httpx)**

* **[nuclei](https://github.com/projectdiscovery/nuclei)**