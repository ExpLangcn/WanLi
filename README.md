#WanLi

**[中文文档](README_CN.md)** ｜[LICENSE](LICENSE) ｜ **[WanLi-ExpLang](https://twitter.com/ExpLang_Cn)** ｜ **[Help](https://github.com/ExpLangcn/WanLi/wiki/Help)**
----

It is convenient for red team personnel to conduct security detection on the target site and quickly obtain assets.

* Asset search detection using FOFA
* Asset search detection using 360 Quake
* Use Ksubdomain for domain fuzzing
* Use Httpx for domain name information detection
* Exploitation and detection using Nuclei

# demo

[![asciicast](https://asciinema.org/a/461330.svg)](https://asciinema.org/a/461330)

# use
````
git clone https://github.com/ExpLangcn/WanLi.git
cd WanLi & pip3 install -r requirements.txt
vim config/config.yaml
````
**[Help](https://github.com/ExpLangcn/WanLi/wiki/Help---%E5%B8%AE%E5%8A%A9)**
````
python3 WanLi.py -h
````

# help

````
optional arguments:
  -h, --help        show this help message and exit
  -fofa FOFA        使用 FOFA 进行关键字搜索 / Keyword search using FOFA.
  -fdomain FDOMAIN  使用 FOFA 进行子域检测 / Subdomain Detection Using FOFA.
  -fl FL            修改 FOFA 的 Limits 配置 / Modify the Limits configuration of FOFA.
  -quake QUAKE      使用 Quake 进行关键字搜索 / Keyword search using Quake.
  -qdomain QDOMAIN  使用 Quake 进行子域检测 / Subdomain Detection Using Quake.
  -ql QL            修改 Quake 的 Limits 配置 / Modify the Limits configuration of Quake.
  -domain DOMAIN    使用 FOFA、Quake、ksubdomain 进行全面的子域检测 / Comprehensive subdomain detection using FOFA, Quake, ksubdomain.
  -pocscan POCSCAN  使用Nuclei对目标进行全部漏洞扫描漏洞检测 / Vulnerability Scanning All Vulnerability Detection on Targets Using Nuclei.
  -lscan LSCAN      使用Nuclei对文件内的目标进行全部漏洞扫描漏洞检测 / Vulnerability Scanning All Vulnerability Detection for Targets in Files Using Nuclei.
````

# update log

````
2022.2.16:
    - Refactor to rewrite WanLiScan
    - Fixed FOFA asset search issue
    - Added FOFA domain name detection
    - Added 360 Quake asset search
    - Added 360 Quake domain name detection
    -Added comprehensive domain name fuzz detection
    - Added vulnerability library single target vulnerability scanning function
    - Added vulnerability library batch target vulnerability scanning function
2022.2.8:
    - Update Docker version

2022.2.x:
    - I forgot the time...
````

# BiLiBiLi

**[RedCodeTm](https://space.bilibili.com/392628031)**

**[Use demo video](https://www.bilibili.com/video/BV1yL4y1376F/)**

#twitter

[@ExpLang_Cn](https://twitter.com/ExpLang_Cn)

### We chat number

![WechatIMG408](img/WechatIMG408.jpeg)

# Info

* **[ksubdomain](https://github.com/boy-hack/ksubdomain)**

* **[httpx](https://github.com/projectdiscovery/httpx)**

* **[nuclei](https://github.com/projectdiscovery/nuclei)**