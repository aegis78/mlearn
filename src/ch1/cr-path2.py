from urllib.parse import urljoin

base = "http://www.naver.com/test.html"

print(urljoin(base, "../c.html"))
print(urljoin(base, "https://www.daum.net/t.html"))
print(urljoin(base, "//nate.com/ab.html"))