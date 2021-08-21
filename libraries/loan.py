from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
from dotenv import load_dotenv
import os
import time
import re

load_dotenv(verbose=True)
chrome_driver_dir = os.getenv('CHROME_DRIVER_DIR')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
wd = webdriver.Chrome(chrome_driver_dir, options=options)

def merge_data(lst):
  new_lst=[lst[0]]

  for v in lst[1:]:
    flag = True
    for i in new_lst:
      if i['title'] == v['title'] and i['author'] == v['author']:
        i['available'] += v['available']
        i['link'] = i['link'] + '+' + v['link']
        flag = False
        break
    if flag:
      new_lst.append(v)

  return new_lst

def search_book_library(keyword):
  wd.get('https://library.korea.ac.kr/datause/advanced-search/advanced-search-form/')

  name_input = wd.find_element_by_css_selector('#item-search-keyword-1')
  name_input.send_keys(keyword)
  search_button = wd.find_element_by_css_selector('#post-191 > div > div > div > form > div.field-group.text-center > button')
  search_button.click()

  time.sleep(1)

  html = wd.page_source
  soup = BeautifulSoup(html, 'html.parser')
  items = soup.select('#post-193 > div.entry-content > div.content > div > div > div.col-lg-9 > div.items.list > div.item.book')

  for i in range(1, len(items)+1):
    a = wd.find_element_by_css_selector('div.item-data.d-flex > div.item-meta > div#item-{0}-location > div.item-loc-triggers > a'.format(i))
    wd.execute_script("arguments[0].click();", a)
  
  html = wd.page_source
  soup = BeautifulSoup(html, 'html.parser')
  items = soup.select('#post-193 > div.entry-content > div.content > div > div > div.col-lg-9 > div.items.list > div.item.book')
  lst = []

  for item in items:
    loan_available = 0
    dic = {}
    title = item.select_one('div.item-data.d-flex > div.item-meta > div.item-title').text
    author = item.select_one('div.item-data.d-flex > div.item-meta > div.item-author').text
    link = item.select_one('div.item-data.d-flex > div.item-cover > a').attrs['href']
    try:
        img_link = item.select_one("div.item-data.d-flex > div.item-cover > a > div").attrs['style']
        img_link = re.findall('\(([^)]+)', img_link)
        if img_link[0][0] != 'h': img_link=["No Image"]
    except:
        img_link = ["No Image"]
    dic['title'] = title.strip()
    dic['author'] = author.strip()
    dic['link'] = link.strip()
    dic['img_link'] = img_link[0]
    cols = item.select("div.item-data.d-flex > div.item-meta > div.item-loc > div.item-loc-contents > div > div > table > tbody")
    for col in cols:
        status = col.select("tr > td")[4].text.split()
        if status[1] == '대출가능': loan_available += 1
    dic['available'] = loan_available
    lst.append(dic)

  if lst:
    lst = merge_data(lst)

  return lst

def status_book_library(link):
  links = link.split('+')
  lst = []
  for link in links:
    detail_link = "https://library.korea.ac.kr"+link
    wd.get(detail_link)
    html = wd.page_source
    soup = BeautifulSoup(html, 'html.parser')
    details = soup.select("#locs-1 > div > table > tbody > tr")

    for detail in details:
      dic = {}
      tds = detail.select("td")
      for i in range(1, 6):
        col = tds[i].text.split()
        if col[0] == '청구기호':
          cols = ''
          for i in range(1, len(col)):
            cols = cols + ' ' + col[i]
          dic[col[0]] = cols.lstrip()
        else:
          dic[col[0]] = col[1]
          if col[0] == '도서상태' and col[1] != '대출중':
            break
      lst.append(dic)

  return lst
