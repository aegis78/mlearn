from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# urlopen으로 메모리 로드
res = req.urlopen(url)

# beautifulsoup 으로 html parse
soup = BeautifulSoup(res, 'html.parser')

# 원하는 데이터 추출하기
title = soup.find("title").string
wf = soup.find("wf").string

print(title)
print(wf)
