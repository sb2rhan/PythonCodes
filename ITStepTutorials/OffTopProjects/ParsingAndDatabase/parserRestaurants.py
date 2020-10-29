# 4. Спарсить названия ресторанов со страницы сайта https://restoran.kz/restaurant  и собрать все рестораны.
import requests
import re
from bs4 import BeautifulSoup
from time import sleep


HOST = 'https://restoran.kz'
URL = 'restaurant'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Connection': 'keep-alive'
}

def get_html(url):
    # getting response by address 'https://restoran.kz/restaurant'
    response = requests.get(url, headers=HEADERS)
    text = response.text
    response.close()
    return text

def parse_page_of_restaurants(page = 1):
    bs = BeautifulSoup(get_html(HOST + '/' + URL + '?page=' + str(page)), 'html.parser')
    # print(bs.prettify())

    restaurant_divs = bs.findAll('div', class_='place-list-card__body')
    # print(restaurant_divs)

    result = []
    for restaurant in restaurant_divs:
        # main info
        h3 = restaurant.find('h3', class_ = 'h2 place-list-card__title')
        phone_block = restaurant.find('div', class_ = 'phones-block')
        phonenumdiv = 'no phone number'
        if (phone_block != None):
            phonenumdiv = phone_block.find('div', class_ = 'phones-block__wrap').text
        
        # additional infos
        place_p = restaurant.find('p', class_ = 'place-list-card__subtitle')
        div_info = restaurant.find('div', class_ = 'list-unstyled mb-4')
        infos_li = div_info.findAll('li', class_ = 'd-flex mr-5 mb-3')

        result.append({
            'Название': h3.text,
            'Ссылка': HOST + h3.find('a', class_ = 'link-inherit-color').get('href'),
            'Номер телефона': phonenumdiv,
            'Адрес': place_p.text,
            'Кухня': infos_li[0].text if len(infos_li) > 0 else 'unknown',
            'Примерная цена': infos_li[1].text if len(infos_li) > 1 else 'no price',
            'Дополнительно': infos_li[2].text if len(infos_li) > 2 else 'no extras'
        })
    return result

# print(parse_page_of_restaurants(2))

def get_max_page(page: int) -> int:
    html = get_html(HOST + '/' + URL + '?page=' + str(page))
    bs = BeautifulSoup(html, 'html.parser')
    paginations = bs.find('ul', class_='pagination')
    # print(paginations)

    pattern = re.compile(r'\d+')
    pages = pattern.findall(paginations.text)
    
    # map converts str pages to int pages
    # then we collect them to list and find the max value 
    max_page = max(list(map(int, pages)))
    # print(max_page)

    if page < max_page:
        return get_max_page(max_page)
    return max_page

def get_all_restaurants() -> list:
    max_page = get_max_page(1)
    # print(max_page)

    result = []
    for page in range(1, max_page + 1):
        result.extend(parse_page_of_restaurants(page))

    return result

print(get_all_restaurants())
