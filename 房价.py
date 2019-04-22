import requests
from bs4 import BeautifulSoup
import re
import openpyxl

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    res = requests.get(url,headers=headers)
    return res

def find_data(res):
    data = []
    soup = BeautifulSoup(res.text,'lxml')
    content = soup.find('div',id='Cnt-Main-Article-QQ')
    target = content.find_all('p',style='TEXT-INDENT: 2em')
    target = iter(target)
    for each in target:
        if each.text.isdigit():
            data.append([\
                re.search((r'\[(.+)\]'),next(target).text).group(1),\
                re.search((r'\d.*'),next(target).text).group(),\
                re.search((r'\d.*'),next(target).text).group(),\
                re.search((r'\d.*'),next(target).text).group()])       
    return data      

def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['城市','房价','工资','房价工资比'])
    for each in data:
        ws.append(each)

    wb.save('2017年中国主要城市房价工资比排行榜.xlsx')


def main():
    url = r'https://news.house.qq.com/a/20170702/003985.htm'
    res = open_url(url)
    
    to_excel(find_data(res))
       
    
if __name__ == '__main__':
    main()
