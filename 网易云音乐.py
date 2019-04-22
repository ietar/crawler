import requests
import json
# from bs4 import BeautifulSoup

def open_url(url):
    name_id = url.split('=')[1]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Referer': 'https://music.163.com/song?id={}'.format(name_id)}

    target_url = r'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)

    params = r'5VmLhYw/VGeg26QJgUtSOhEzWhqRcqVu7CmbhZLhaTCXFIWimW3PiH7z8/nnQ4ZYbnRJBo/GpriiZE888YkS+iinsgmNmINOurFf56KwAcuC3wHU1edUt3zp+b0j1rws9Df86lDc3+FAWj1cC7lAh35o73Tim0lJIzYrtctelyL60Wdh7oqnFMvf+nhcVtk9'
    encSecKey = r'3206c885767929f19398b403166868ff3d01c373b69fc0bb37e53a5ecfc04e44407c4343f8dfe004dde784308b38e22e9daeaa99c107273fed19fac999dae004cb0b042d77a4983acb9627d1e197253d65b9457a31f207cd1520cf61d921f350203b0cacfc1c11725297ba77df10f3857ccad1fdf39d118be4573cbe1e707170'
    data = {
        'params':params,
        'encSecKey':encSecKey}
    
    res = requests.post(target_url,headers=headers,data=data,timeout=3)    
    return res


def get_comments(res,name_id):
    comments_json = json.loads(res.text)   
    hot_comments = comments_json['hotComments']
    
    with open('comments_of {}.txt'.format(name_id),'w',encoding='utf-8') as f:
        if hot_comments:
            f.write('精彩评论:'+'\n')
            f.write('--------------------------------------------------------\n')
            for each in hot_comments:
                f.write(each['user']['nickname']+':\n\n')
                f.write(each['content']+'\n')
                f.write('----------------------------\n')  
        # 无论有没有精彩评论 都记录最新评论
        f.write('\n'+'最新评论:'+'\n')
        f.write('--------------------------------------------------------\n')
        for each in comments_json['comments']:
            f.write(each['user']['nickname']+':\n\n')
            f.write(each['content']+'\n')
            f.write('----------------------------\n')


def main():
    
    # url = r'https://music.163.com/#/song?id=4466775'
    url = input('请输入链接地址:')
    name_id = url.split('=')[1]
    res = open_url(url)  
    get_comments(res,name_id)
    
    return

    
if __name__ == '__main__':
    main()

 
