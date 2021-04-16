import requests
from lxml import etree
import csv
import time
import socket
from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio


def main(url):
    html = etree.HTML(r.content.decode())
    html_list = html.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[1]')
    mp4_list = []
    jpg_list = []
    for i in html_list:
        hd_img = i.xpath('./div[2]/div/a/@href')[0]  # 高清图片
        # sd_img = i.xpath('./div[3]/a/@href')
        img_name1 = i.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/p[1]/a/text()')[0]
        img_name2 = i.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/p[2]/a/text()')[0]
        jpg_list.append(hd_img)
        try:
            dt_img = i.xpath('./div[4]/a[@target="_blank"]/@href')[0]  # 动态图片
            mp4_list.append(dt_img)
        except IndexError:
            pass
        try:
            for i in mp4_list:
                rm = requests.get(i)
                r.close()
                with open('mp4/LOL/' + img_name1 + img_name2 + '.mp4', 'wb')as f:
                    f.write(rm.content)
                    f.close()
        except:
            pass
    for j in jpg_list:
        print(img_name1 + img_name2 + '正在下载')
        rj = requests.get(j)
        r.close()
        with open('img/LOL/' + str(num) +'.'+img_name1 + img_name2 + '.jpg', 'wb')as f:
            f.write(rj.content)
            f.close()
        print(img_name1 + img_name2 + '下载成功')


if __name__ == '__main__':
    num = 555
    socket.setdefaulttimeout(20)
    for i in range(556, 999):
        num = num + 1
        url = f'https://www.ghostoact.com/arts/models/?cp={i}&sk=0'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Cookie': 'PHPSESSID=onk0bg4156vs3hpub19bduc2j1; UM_distinctid=178b46a516884d-03765b43f0672f-c3f3568-1fa400-178b46a51699f9; CNZZDATA1259919941=1260500648-1617931463-https%253A%252F%252Fwww.ghostoact.com%252F%7C1617965259'
        }
        r = requests.get(url=url,headers=headers)
        if r.status_code == 500:
            print('图片资源加载中')
            continue
        for j in range(30):
            url = f'https://www.ghostoact.com/arts/models/?cp={i}&sk={j}'
            try:
                r = requests.get(url=url, headers=headers)
                r.close()
                if r.status_code == 500:
                    print('图片资源加载中')
                    continue
                main(url)
            except:
                print('下载失败')
