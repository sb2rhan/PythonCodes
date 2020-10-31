# 1. Спарсить названия ресторанов со страницы сайта https://restolife.kz/restoran/. Собрать все рестораны в базу.
import requests
import re
from bs4 import BeautifulSoup


HOST = 'https://restolife.kz'
URL = 'restoran'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Connection': 'keep-alive'
}

def get_page(url: str) -> str:
    response = requests.get(url, headers=HEADERS)
    text = response.text
    response.close()
    return text


def get_restaurants_from_page(page: int) -> list:
    html_bs = BeautifulSoup(get_page(HOST + '/' + URL + '/' + ('' if page==1 else f'page-{page}/')), 'html.parser')
    # print(html_bs.prettify())
    restaurant_divs = html_bs.findAll('div', class_='cat-item')
    # print(restaurant_divs)
    ready_restaurants = []
    for restaurant_div in restaurant_divs:
        title = restaurant_div.find('h2')
        link = title.find('a').get('href')
        category = restaurant_div.find('div', class_='category')
        rating = restaurant_div.find('div', class_='rate-block rate-main rate-tooltip').find('div', class_='total')

        extras_raw = restaurant_div.findAll('span', class_='rate-tooltip-block rate-tooltip-block_text rate-tooltip-block_left')
        extras = [ extras_raw[i].text for i in range(len(extras_raw)) ]

        ready_restaurants.append({
            'Title': title.text.replace('\n', ''),
            'Link to website': HOST + link,
            'Category': category.text if category != None else 'No categories',
            'Rating': rating.text if rating != None else 'No ratings',
            'Extras': extras if len(extras) > 0 else 'No extras'
        })
    
    return ready_restaurants


def get_max_page():
    link = HOST + '/' + URL + '/'
    html_bs = BeautifulSoup(get_page(link), 'html.parser')
    navbar = html_bs.find('nav', class_='pagenav')
    pages = navbar.findAll('a')

    max_page = int(pages[len(pages) - 1].text)
    return max_page


def get_all_restaurants():
    max_page = get_max_page()

    all_results = []
    for page in range(1, max_page + 1):
        all_results.extend(get_restaurants_from_page(page))
    
    return all_results

# print(get_all_restaurants()) # uncomment it to see result
