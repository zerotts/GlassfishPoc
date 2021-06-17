#-*- coding: utf-8 -*-
import base64
import sys
import time
import requests
from lxml import  etree
type=sys.getfilesystemencoding()

'''如何实现这个漏洞批量化
1、获取到可能存在漏洞的地址信息-借助fofa进行目标获取
    将请求到的数据进行筛选
2、批量请求地址信息进行判断是否存在--单线程和多线程'''
#https://fofa.so/result?qbase64=ImdsYXNzZmlzaCIgJiYgcG9ydD0iNDg0OCI%3D
#serch_data='"glassfish" && port="4848" && country="CN"'
#设置cookie，以便于翻页
def search(serch_data):
    headers={
        'cookie':'befor_router=%2Fresult%3Fqbase64%3DImdsYXNzZmlzaCIgJiYgcG9ydD0iNDg0OCI%253D; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTA4NDk0LCJtaWQiOjEwMDA2NTU0MSwidXNlcm5hbWUiOiJ6ZXJvdHRzIiwiZXhwIjoxNjIzMjY0NTAzfQ.6Wf13FepVT7BvpWts8KHw_etljJHE0UTn74wzbUCTd52AL5224NB8kKiJjs9fmLLmKxCquZROdWYRJD6YRRXhA; user=%7B%22id%22%3A108494%2C%22mid%22%3A100065541%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22zerotts%22%2C%22nickname%22%3A%22zerotts%22%2C%22email%22%3A%22om2bg0ak795mzlpyj5jeql7arw7y%40open_wechat%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FDYAIOgq83erib9vfNJf36KmOpOAOXOvQyp1Lq3hllRP6ic2hQHuFGnTfNW1vkvJKFwwDlZg73WYcjeynu3PfbbAw%2F132%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FDYAIOgq83erib9vfNJf36KmOpOAOXOvQyp1Lq3hllRP6ic2hQHuFGnTfNW1vkvJKFwwDlZg73WYcjeynu3PfbbAw%2F132%22%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22rank_level%22%3A0%2C%22company_name%22%3A%22zerotts%22%2C%22coins%22%3A0%2C%22credits%22%3A0%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A1623221303%7D; refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTA4NDk0LCJtaWQiOjEwMDA2NTU0MSwidXNlcm5hbWUiOiJ6ZXJvdHRzIiwiZXhwIjoxNjIzNDgwNTAzLCJpc3MiOiJyZWZyZXNoIn0.N13YWB-_uj6SzSFkskJaO3koSAvl8McFybj7xqqqsKRqY0OJ8QokjLRjXj8fwBbJg5S-c5C2yeExzG2LE9yAog; Hm_lvt_b5514a35664fd4ac6a893a1e56956c97=1623198402,1623199631,1623221273,1623229725; Hm_lpvt_b5514a35664fd4ac6a893a1e56956c97=1623229728',
    }
    num=0
    for yeshu in range(1,6):
        #拼接爬取的url
        serch_data_bs=str(base64.b64encode(serch_data.encode("utf-8")).decode('utf-8'))
        url_1='https://fofa.so/result?page='+str(yeshu)+'&qbase64='
        url_2=url_1+serch_data_bs
        try:
            #请求url并获取url中的内容
            result=requests.get(url_2,headers=headers).content
            #print (result.decode('utf-8'))
            #etree.HTML解析字符串格式的html文档对象，如果想通过xpath获取html源码中的内容，就要先将html源码转换成_Element对象
            soup=etree.HTML(result)
            #<a href="http://3.26.102.85:4848" target="_blank">3.26.102.85
            ip_data=soup.xpath('//span[@class="aSpan"]/a[@target="_blank"]/@href')#提取并过滤数据中的内容
            ip_data='\n'.join(ip_data)
            print ("正在提取第").decode('utf-8').encode(type),yeshu,("页").decode('utf-8').encode(type)
            print ("ip_data:"),ip_data
            #通过文件读写操作，将ip_data的数据写入到ip_data.txt中
            with open(r'ip_data.txt','a+') as f:
                f.write(ip_data+'\n')
                f.close()
            num=num+1
        except Exception as e:
            time.sleep(0.5)
            pass
    print ("num:"),num
if __name__ == '__main__':
    data_1=sys.argv[1]
    search(data_1)