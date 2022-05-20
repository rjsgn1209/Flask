from flask  import Flask, render_template

app = Flask(__name__)

import requests 
from bs4 import BeautifulSoup

from selenium import webdriver
import time

@app.route('/')
def home():
    return "home"


@app.route('/daum_news')
def daum():
    url = 'https://www.daum.net'

    driver = webdriver.Chrome()

    time.sleep(1)
    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    myList = []

    items = soup.select('#news > div.news_prime.news_tab1 > div > div > ul > li > a')
    
    for i in items:
        myList.append(i.text)
        #print(i.text)
        
    driver.close()
    print(myList)
    return render_template('index1.html', list=myList)

@app.route('/about')
def about():
    return "about page입니다.."


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
    