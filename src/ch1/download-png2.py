import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
saveName = "test1.png"

mem = urllib.request.urlopen(url).read()

with open(saveName, mode="wb") as f:
    f.write(mem)
    print("저장 되었습니다..!")

