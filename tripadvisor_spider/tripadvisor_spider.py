import requests
from bs4 import BeautifulSoup
import time
import json

main_url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"



def make_cate_arr(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    cates = soup.select("div.shelf_title_container > a")
    #  类目
    cate_arr = []
    for cate in cates:
        line = {
            "cate_text": cate.get_text(),
            "href": main_url + str(cate.get("href")),
            "cate_arr": []
        }
        cate_arr.append(line)
    return cate_arr



def get_cate_content(href):
    time.sleep(2)
    arr = []
    res = requests.get(href)
    soup = BeautifulSoup(res.text, "lxml")

    titles =  soup.select("div.listing_title > a")
    stars = soup.select("span.ui_bubble_rating")
    watchs = soup.select("div.rating span.more >  a")
    imgs = soup.select("img.photo_image")


    for title, star, watch, img  in  zip(titles, stars, watchs, imgs):
        data = {
            "title": title.get_text(),
            "star": star.get("class")[1].split("_")[1],
            "watch": watch.get_text().strip().split("条点评")[0],
            "img_url": img.get("src")
        }
        arr.append(data)
        print(arr)

    return arr


cate_arr = make_cate_arr(main_url)
for cate in cate_arr:
    if(cate["href"]):
        cate["cate_arr"] = get_cate_content(cate["href"])


with open('test.json','w') as fileobj:
    json.dump(cate_arr, fileobj)
    print('结束了')