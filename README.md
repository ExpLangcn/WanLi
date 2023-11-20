# WanLi Scan - 转Go 不再维护Python项目

**[中文说明](README_CN.md)** ｜ **[许可证](许可证)**｜**[帮助](https://github.com/ExpLangcn/WanLi/wiki)**
----

It is convenient for red team personnel to conduct security detection on the target site and quickly obtain assets.

* Asset search detection using FOFA
* Asset search detection using 360 Quake
* Use Ksubdomain for domain fuzzing
* Use Httpx for domain name information detection
* Exploitation and detection using Nuclei
* Daily automatic update of vulnerability library

## 法律免责声明
本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建靶机环境。
在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。
如果发现上述禁止行为，我们将保留追究您法律责任的权利。

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任.
您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。

# Function

![image-20220224174705312](img/e6c9d24egy1gzoquvn5grj21gu0pmgp3.jpg)

- [x] call FOFA service for asset detection

![image-20220224174726404](img/e6c9d24egy1gzoqv8r7okj21am0fidhl.jpg)

![image-20220224174250975](img/e6c9d24egy1gzoqqh5b0kj21hq0sawkr.jpg)

- [x] Automatic vulnerability scanning for FOFA asset detection results

![image-20220224174351014](img/e6c9d24egy1gzoqric1naj21h80r8n44.jpg)

![image-20220224170851426](img/e6c9d24egy1gzopr3lvg5j21hm0dcdkk.jpg)

- [x] Call Quake service for asset detection

Like the FOFA effect, Quake is currently being updated and upgraded, so let's not post the screenshot of the effect.

- [x] Automatic vulnerability scanning for Quake asset detection results

Like the FOFA effect, Quake is currently being updated and upgraded, so let's not post the screenshot of the effect.

- [x] Subdomain detection on target

![image-20220224174751261](img/e6c9d24egy1gzoqvo7opqj21gw0hgwh0.jpg)

![image-20220224171202785](img/e6c9d24egy1gzopufl9a4j21hm0lcdlj.jpg)

- [x] Automatic vulnerability scanning for subdomain detection results

![image-20220224171403743](img/e6c9d24egy1gzopwj1bf1j21ho0m20z4.jpg)

- [x] The program adapts to Windows, Macos, Linux systems

Configure `system` on the third line of the `config/config.yaml` file

![image-20220224171426738](img/e6c9d24egy1gzopwwimqyj20uy01o3yq.jpg)

- [x] Interactive control usage

![image-20220224174700727](img/e6c9d24egy1gzoqute7hnj21gu0pmgp3.jpg)

- [ ] Call HUNTER service for asset detection
- [ ] Vulnerability scan on HUNTER asset detection results
- [ ] Call ARL for asset detection
- [ ] Vulnerability scan on ARL asset results
- [ ] Develop WEB visual interface

# use

````
git clone https://github.com/ExpLangcn/WanLi.git
cd WanLi & pip3 install -r requirements.txt
vim config/config.yaml # Configure FOFA information and Quake information
````

**[帮助](https://github.com/ExpLangcn/WanLi/wiki)**

````
python3 WanLi.py # Enter interactive mode and enter Help to view help information
````

# update log

````
2022.2.24:
- Adapt to Windows system
- Restore interactive control, remove parameter control
- Optimize the overall code to improve efficiency
2022.2.21:
    - config problem report error solution, more suitable for Windows system
    - Removed the Domain scan function of FOFA and Quake and merged it into the Domain parameter
    - Improve the vulnerability scanning function, the vulnerability database will be updated before each vulnerability scan
    - replace the pocscan parameter with the poc parameter
    - To perform vulnerability scanning on Domain results and asset detection results, just add -scan
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

#### 😄 I’m ExpLang [**Twitter**](https://twitter.com/ExpLang_Cn) 欢迎关注fo～


# We chat number

![WechatIMG408](img/WechatIMG408.jpeg)

# Info

* **[ksubdomain](https://github.com/boy-hack/ksubdomain)**

* **[httpx](https://github.com/projectdiscovery/httpx)**

* **[nuclei](https://github.com/projectdiscovery/nuclei)**
