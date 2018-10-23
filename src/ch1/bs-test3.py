# 라이브러리 읽어들이기
from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
<ul>
    <li><a href="http://www.naver.com">naver</li>
    <li><a href="http://www.daum.net">daum</li>
</body></html>
"""

# HTml 분석하기
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출하기
links = soup.find_all("a")

for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)


