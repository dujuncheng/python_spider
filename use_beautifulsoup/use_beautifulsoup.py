from bs4 import BeautifulSoup

PATH = './1_2_homework_required/index.html'

with open(PATH, 'r') as homework:
    Soup = BeautifulSoup(homework,'lxml')
    titles =  Soup.select('div.caption > h4 > a')
    prices = Soup.select('h4.pull-right')
    imgs = Soup.select('.thumbnail > img')
    stars = Soup.select('.ratings > p:nth-of-type(2)')


    for title, price, img, star in zip(titles, prices, imgs ,stars):
        data = {
            'title': title.get_text().strip(),
            'price': price.get_text().strip(),
            'img': img.get('src'),
            'star': len(star.find_all('span', class_='glyphicon glyphicon-star'))
        }
        print(data)


