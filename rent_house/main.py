import requests
from bs4 import BeautifulSoup
import time
import json
import xlwt

import choose_ip

ip = choose_ip.get_ip()




main_url = "https://bj.lianjia.com/zufang/pg2/"

#完善的headers
target_headers = {'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer':'http://www.xicidaili.com/nn/',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
}




def get_content(item):
    titles = item.select('div.info-panel > h2 > a')
    wheres = item.select('div.info-panel div.where a span')
    zones = item.select('div.info-panel span.zone span')
    meters = item.select('div.info-panel span.meters')
    subways = item.select('div.info-panel .chanquan span.fang-subway-ex span')
    haskey = item.select('div.info-panel .chanquan span.haskey-ex span')
    decoration = item.select('div.info-panel .chanquan span.decoration-ex > span')
    heating = item.select('div.info-panel .chanquan span.heating-ex span')
    price = item.select('div.price span.num')
    update = item.select('div.price-pre')
    look = item.select('div.square span.num')

    data = {
        'title': titles[0].get_text().strip() if len(titles) > 0 else '',
        'where': wheres[0].get_text().strip() if len(wheres) > 0 else '',
        'zone': zones[0].get_text().strip() if len(zones) > 0 else '',
        'meter': meters[0].get_text().strip() if len(meters) > 0 else '',
        'subway': subways[0].get_text().strip() if len(subways) > 0 else '',
        'haskey': haskey[0].get_text().strip() if len(haskey) > 0 else '',
        'decoration': decoration[0].get_text() if len(decoration) > 0 else '',
        'heating': heating[0].get_text().strip() if len(heating) > 0 else '',
        'price': price[0].get_text().strip() if len(price) > 0 else '',
        'update': update[0].get_text().strip() if len(update) > 0 else '',
        'look': look[0].get_text().strip() if len(look) > 0 else '',
    }
    return data


def get_page(url):
    arr = []
    time.sleep(2)
    res = requests.get(url, headers=target_headers)
    soup = BeautifulSoup(res.text, 'lxml')
    # 所有的一块一块的租房信息
    items = soup.find_all(attrs={"data-el": "zufang"})
    for item in items:
        data = get_content(item)
        arr.append(data)
        print(data)
    return arr

def save_one_page(arr, start, worksheet):
    try:
        for i in range(len(arr)):
            values = list(arr[i].values())
            for x in range(len(values)):
                start_index = i + start
                print( 'start_index' + str(start_index) )
                worksheet.write(start_index, x, str(values[x]))  # 不带样式的写入
        print('success')
    except:
        print('fail in writinge')


def get_and_save (num) :
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('page')
    for i in range(num):
        url = 'https://bj.lianjia.com/zufang/pg' + str(i)+ '/'
        try:
            one_page_arr = get_page(url)
            save_one_page(one_page_arr, (i)*30, worksheet)
        except:
            print('fail in wrap')

    workbook.save('5000页的数据.xls')


get_and_save(5000)







