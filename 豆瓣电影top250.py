import requests
from bs4 import BeautifulSoup
import re
import time


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
url = r'https://movie.douban.com/top250'
res = requests.get(url,headers=headers,timeout=1)
soup = BeautifulSoup(res.text,'lxml')

pages = 1
bonus_url = r'?start=25&filter='
list0=[]
list1=[]
list2=[]
list3=[]
list4=[]
sumary = []
url_new = url

while pages <= 10:
    res = requests.get(url_new,headers=headers,timeout=1)
    soup = BeautifulSoup(res.text,'lxml')
    print('正在爬取第 {} 页'.format(pages))

    item = 0
    target = soup.find('div',class_='article').find_all('li')
    # 拆出每一块
    for i in range(25):
        # 排名
        list0.append(target[i].em.text)

        # 电影名
        list1.append(target[i].find('div',class_='hd').a.span.text)

        # 评分
        list2.append(target[i].find('div',class_='star').find('span',class_='rating_num').text)

        # 资料
        list3.append(''.join((target[i].find('div',class_='bd').p.text.split('\n')[1].strip(),\
                     target[i].find('div',class_='bd').p.text.split('\n')[2].strip())))
        # 简介
        if target[i].find('span',class_='inq') != None: 
            list4.append(target[i].find('span',class_='inq').text)
        else:
            list4.append('')

    # 有些没简介的会搞乱list4 重写逻辑
            
    bonus_url = re.sub('\d+',str(25*pages),bonus_url)
    pages += 1
    url_new = ''.join((url,bonus_url))                    
    time.sleep(0.1)
    


for i in range(len(list1)):
    sumary.append(' '.join((list0[i],list1[i],list2[i],list3[i],list4[i],'\n')))
with open('豆瓣电影top250.txt','w',encoding='utf-8') as f:
    f.writelines(sumary)



    
