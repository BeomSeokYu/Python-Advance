# 벅스 뮤직 차트 스크래핑

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver

'''
벅스 차트
'''

html = requests.get('https://music.bugs.co.kr/chart')
bsObj = bs(html.text, "html.parser")

titles = bsObj.select('.byChart > tbody > tr th p.title > a')
singers = bsObj.select('.byChart > tbody > tr td p.artist > a')
ranks = bsObj.select('.byChart > tbody > tr td > div > strong')

songData = []
for i in range(0, 100):
    title = titles[i].text
    singer = singers[i].text
    rank = ranks[i].text
    songData.append([rank, title, singer])
df = pd.DataFrame(songData, columns=['순위', '타이틀', '가수'])
print(df)


'''
멜론 차트
'''
driver = webdriver.Chrome('chromedriver.exe')           # 크롬을 이용해 불러옴
driver.get('https://www.melon.com/chart/index.htm')

txt = driver.page_source
html = bs(txt)
titles1 = html.select('tbody .rank01 a')
singers1 = html.select('tbody .rank02 a')
ranks1 = html.select('tbody .rank')

songData1 = []
for i in range(0, 100):
    title = titles1[i].text
    singer = singers1[i].text
    rank = ranks1[i].text
    songData1.append([rank, title, singer])
df1 = pd.DataFrame(songData1, columns=['순위', '타이틀', '가수'])
print(df1)


'''
지니 차트
'''
driver = webdriver.Chrome('chromedriver.exe')           # 크롬을 이용해 불러옴
driver.get('https://www.genie.co.kr/chart/top200')

txt = driver.page_source
html = bs(txt)
titles2 = html.select('tbody .info .title')
singers2 = html.select('tbody .info .artist')
ranks2 = html.select('tbody .number')

songData2 = []
for i in range(0, 50):
    title = titles2[i].text.strip()
    singer = singers2[i].text.strip()
    rank = ranks2[i].text[0:3].strip()
    songData2.append([rank, title, singer])
df2 = pd.DataFrame(songData2, columns=['순위', '타이틀', '가수'])
print(df2)