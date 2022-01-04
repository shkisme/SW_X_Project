/*
사용자가 입력한 값 만큼, 멜론 차트 데이터를 불러와 띄운다.
*/

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    RANK = int(input("몇 위까지의 노래를 보고 싶으신가요? ")) # 멜론 차트 순위, 사용자가 원하는 만큼의 차트순위를 입력하는 것이 가능합니다.
    print("-"*50)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
    req = requests.get('https://www.melon.com/chart/index.htm', headers =header) # request라이브러리를 이용하여  원하는 url의 http 요청을 받아옵니다.
    html = req.text # 받아온 데이터를 text로 변환합니다.
    parse = BeautifulSoup(html, 'html.parser') # BeautifulSoup 라이브러리를 이용하여 html로 파싱합니다.
 
    titles = parse.find_all("div", {"class": "ellipsis rank01"}) 
    singers = parse.find_all("div", {"class": "ellipsis rank02"}) 
 
    title = []
    singer = []
 
    for t in titles:
        title.append(t.find('a').text)
 
    for s in singers:
        singer.append(s.find('span', {"class": "checkEllipsis"}).text)
 
    for i in range(RANK):
        print("랭킹 : %d위" % (i + 1))
        print('곡명 : %s' % title[i])
        print('가수 : %s' % singer[i])
        print("-"*50)
