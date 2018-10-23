import urllib.request

# URL과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
saveName = "test.png"

urllib.request.urlretrieve(url, saveName)
print("저장되었습니다..!")