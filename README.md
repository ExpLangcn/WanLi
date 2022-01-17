# WanLi

**[中文版](README_CN.md)** ｜[LICENSE](LICENSE) ｜ **[WanLi-ExpLang](https://twitter.com/ExpLang_Cn)** ｜ **[Help](https://github.com/ExpLangcn/WanLi/wiki/Help---%E5%B8%AE%E5%8A%A9)**

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
**[Help](https://github.com/ExpLangcn/WanLi/wiki/Help---%E5%B8%AE%E5%8A%A9)**
```
python3 WanLi.py
```
# Help
```
clear                 clear the screen
ddir                  scans sensitive files and sensitive addresses of related domain names and subdomains of a single main domain name, ddir default.com
dirscan               scans sensitive files and sensitive addresses of a single web application, dirscan https://www.default.com/
domain                Scan related domain names and subdomains of a single main domain name, domain default.com
exit                  to exit the tool
help                  List available commands or provide detailed help for a specific command
pocscan               scans single or multiple WEB application vulnerabilities, you can specify vulnerabilities or batch vulnerabilities, please use "*.yaml" for batch vulnerabilities
portscan              detects open ports for a single domain name or IP, portscan default.com
```

# BiLiBiLi

**[RedCodeTm](https://www.bilibili.com/)**

**[Use demo video](https://www.bilibili.com/video/BV1hL411c7XB/)**

# Twitter

**[@ExpLang_Cn](https://twitter.com/ExpLang_Cn)**

# WeChat

![WechatIMG408](img/WechatIMG408.jpeg)

# Info

* **[ksubdomain](https://github.com/knownsec/ksubdomain)**

* **[dirsearch](https://github.com/maurosoria/dirsearch)**

* **[subfinder](https://github.com/projectdiscovery/subfinder)**

* **[httpx](https://github.com/projectdiscovery/httpx)**

* **[nuclei](https://github.com/projectdiscovery/nuclei)**

* **[naabu](https://github.com/projectdiscovery/naabu)**
