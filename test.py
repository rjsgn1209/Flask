from bs4 import BeautifulSoup

from selenium import webdriver
import time

url = 'https://www.daum.net/'
    
driver = webdriver.Chrome()

time.sleep(1)
driver.get(url)
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

items = soup.select('#news > div.news_prime.news_tab1 > div > div > ul > li > a')
print(len(items))
myList = []
#items = soup.select('#news')[0].select('.link_item')
for i in items:
    print(i.text)