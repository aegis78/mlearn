# IP 확인 API로 접근해서 출력하기
import urllib.request as rq

url = "http://api.aoikujira.com/ip/ini"
res = rq.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)
