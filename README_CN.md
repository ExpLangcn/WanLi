# WanLi

**[英文版](README.md)** ｜[LICENSE](LICENSE) ｜ **[WanLi-ExpLang](https://twitter.com/ExpLang_Cn)** ｜ **[Docker](https://github.com/ExpLangcn/WanLi/wiki/DockerHelp)** | **[帮助](https://github.com/ExpLangcn/WanLi/wiki/Help---%E5%B8%AE%E5%8A%A9)**
----

方便红队人员对目标站点进行安全检测，快速获取资产。

* 使用FOFA进行资产搜索探测
* 使用360 Quake进行资产搜索探测
* 使用Ksubdomain进行域名Fuzz
* 使用Httpx进行域名信息探测
* 使用Nuclei进行漏洞利用和检测

# 演示

[![asciicast](https://asciinema.org/a/461330.svg)](https://asciinema.org/a/461330)

# 使用
```
git clone https://github.com/ExpLangcn/WanLi.git
cd WanLi & pip3 install -r requirements.txt
vim config/config.yaml
```
**[Help](https://github.com/ExpLangcn/WanLi/wiki/Help---%E5%B8%AE%E5%8A%A9)**
```
python3 WanLi.py -h
```

# 帮助

```
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
```

# 更新日志

```
2022.2.16:
    -重构重写WanLiScan
    -修复FOFA资产搜索问题
    -新增FOFA域名探测
    -新增360 Quake资产搜索
    -新增360 Quake域名探测
    -新增综合性域名Fuzz探测
    -新增漏洞库单个目标漏洞扫描功能
    -新增漏洞库批量目标漏洞扫描功能
2022.2.8:
    -更新Docker版本

2022.2.x:
    -我忘了时间了...
```

# BiLiBiLi

**[RedCodeTm](https://space.bilibili.com/392628031)**

**[使用演示视频](https://www.bilibili.com/video/BV1hL411c7XB/)**

# Twitter

[@ExpLang_Cn](https://twitter.com/ExpLang_Cn)

### 微信号

![WechatIMG408](img/WechatIMG408.jpeg)

# Info

* **[ksubdomain](https://github.com/boy-hack/ksubdomain)**

* **[httpx](https://github.com/projectdiscovery/httpx)**

* **[nuclei](https://github.com/projectdiscovery/nuclei)**