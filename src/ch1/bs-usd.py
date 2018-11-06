import urllib.request
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
reponse = urllib.request.urlopen(url)

soup = BeautifulSoup(reponse, "html.parser")
results = soup.select("ul.data_lst > li")

for result in results:
    print(result)


for result in results:
    nation = result.select_one("h3 > span.blind")
    value = result.select_one("span.value")
    change_num = result.select_one("span.change")
    change_txt = result.select_one("div > span.blind")

    print(nation.string, value.string + "원", change_num.string, change_txt.string)










