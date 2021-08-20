from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
import time


def search_book_library(keyword):
  chrome_driver_dir = '/Users/sangyuplee/KoreaUniv/DevKor/bookitout/chromedriver'
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  wd = webdriver.Chrome(chrome_driver_dir, options=options)
  wd.get('https://library.korea.ac.kr/datause/advanced-search/advanced-search-form/')

  name_input = wd.find_element_by_css_selector('#item-search-keyword-1')
  name_input.send_keys(keyword)
  search_button = wd.find_element_by_css_selector('#post-191 > div > div > div > form > div.field-group.text-center > button')
  search_button.click()

  time.sleep(1)

  html = wd.page_source
  soup = BeautifulSoup(html, 'html.parser')
  items = soup.select('#post-193 > div.entry-content > div.content > div > div > div.col-lg-9 > div.items.list > div.item.book')
  list = []

  for item in items:
    dic = {}
    title = item.select_one('div.item-data.d-flex > div.item-meta > div.item-title').text
    author = item.select_one('div.item-data.d-flex > div.item-meta > div.item-author').text
    link = item.select_one('div.item-data.d-flex > div.item-cover > a').attrs['href']
    dic['title'] = title.strip()
    dic['author'] = author.strip()
    dic['link'] = link.strip()
    list.append(dic)
    # print(title.strip())
    # print(author.strip())
    # print(link)
    # print('=========================')

  return list