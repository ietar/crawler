import requests
import re
import json

def count_sales(items):
    count = 0
    for i in items:
        if '小甲鱼' in i['title']:
            count += int(re.search(r'\d+',i['view_sales']).group())
    return count

def get_items(res):
    g_page_config = re.search(r'g_page_config = (.*?);\n',res.text)     
    page_config_json = json.loads(g_page_config.group(1))
    # 大小小小字典page_config_json
    page_items = page_config_json['mods']['itemlist']['data']['auctions']
    result = []
    for i in page_items:
        dict1 = dict.fromkeys(('nid','title','detail_url','view_price','view_sales','nick'))
        dict1['nid'] = i['nid']
        dict1['title'] = i['title']
        dict1['detail_url'] = i['detail_url']
        dict1['view_price'] = i['view_price']
        dict1['view_sales'] = i['view_sales']
        dict1['nick'] = i['nick']
        result.append(dict1)
    return result


def open_url(keyword):
    '''需手动更新cookie'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'cookie':'miid=525117005502861390; t=ed7c6238aa6b191f608a4850db7799b1; cna=Hr3/FMGiyTcCATwKpP3GM0t7; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; tg=0; enc=3xAHmgx0rlTGRS%2Fx%2FhllrG%2F3YqFqkbeEVKNCIX5WS1gJpPjWu9bF%2B23xVHytRG57l5g7ePIgaRxcOiEkTZ33Tw%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D1%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=1a93048bd2748d7699f25680d1c65d4d; v=0; _tb_token_=e5330618ee318; unb=1014129895; sg=153; _l_g_=Ug%3D%3D; skt=bf61a62072ec6f57; cookie1=BvXlp6FzTnVR5EJJWYWjS8pSUYdIFDCSzljzsNogeB0%3D; csg=c784490d; uc3=vt3=F8dByEfL%2FLeQomtR7OI%3D&id2=UoH%2B4nVjOB1kyg%3D%3D&nk2=CsOJlqLE&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTU1NTQ4ODYzMg%3D%3D; tracknick=ietar1; lgc=ietar1; _cc_=URm48syIZQ%3D%3D; dnk=ietar1; _nk_=ietar1; cookie17=UoH%2B4nVjOB1kyg%3D%3D; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVLhR&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ4SECaFtqtg%3D%3D&tag=8&lng=zh_CN; mt=ci=2_1; JSESSIONID=CCE283FD3E41DB2E6B1F4440A3DE938E; isg=BF9fYp37f6BixHtwuJo6hEx27rMpbLMd6cQtGfGs-45VgH8C-ZRDtt1SRlBbA4ve; l=bBQIPttlvmk-3b1bBOCanurza77OSIRYYuPzaNbMi_5Qd6TswX_OlarsGF96Vj5RsX8B4R15R8p9-etkZ'
        }
    payload = {'q':keyword,'sort':'sale_desc'}
    url = r'https://s.taobao.com/search'
    res = requests.get(url,headers=headers,params=payload,timeout=3)
    return res


def main():
    keyword =  input('请输入搜索关键词:')
    # keyword = '零基础入门学习Python'
    res = open_url(keyword)
    result = get_items(res)
    total = count_sales(result)
    print('total is:',total)

if __name__ == '__main__':
    main()
