import requests
import json
import urllib.request
from os import makedirs
import time


def data_request(last_date, last_id, list_size):
    url = "http://cy.cyworld.com/home/22263030/posts"

    querystring = {"folderid": "", "tagname": "", "lastid": last_id, "lastdate": last_date, "listsize": list_size, "homeId": "22263030",
                   "airepageno": "0", "airecase": "D", "airelastdate": "", "searchType": "R", "search": "",
                   "_": "1546929325844"}

    headers = {
        'Cookie': "_ga=GA1.2.705694013.1536899589; UD3=s4c6727a4a1cd8e39152c169f46a68de; UA3=|MjIyNjMwMzA=|; SCOUTER=x8rpgden8uun1; LOGIN=iplevel=2&saveid=off; _gid=GA1.2.1779823346.1546929311; _gat_gtag_UA_64284762_12=1; cookieinfouser=7783dce5a01ebb4988b9a3df43d4b578af96f28a1ce977eeae750e34e5ff1b7e9f4aed7607a4680166f182cbbb0dacf26cf26a993c93dfabf589857bed9dd8ef1a8b8b12e8771524485b2a1dc02b258d1ce70d6fbebd4b2a2cf74d8fad7f66cf8964ed673914a2997d7baafb1d15b1a7d595c11d41b22078c3ccd1b791e4eb3d18b2d520961db56ed873f793ed37e8e9; NSVC=||; CFN=23619c7c5b939a497dbfea0ad05571aba8184ff9732e670bf52f1ce749855fc5414f6082025391735955c64707194cb6690a6697a113a4c072ff3be02184fe930c38e2d06032e5a7b0743c73dca76c6a91f92a458f7051687c665121690222f3bd760a2ea957f783be7d2eeeea0d19576b32a8e786d9630cbd140d851a9ef085359681401004b41fc77e02fc1813ce7fc910be415b8adf30b9ee63901f1cdd97d9713e4a49b32fde4aee2d7ccc13def278fe3c0d3a211430e8e4c2326f2f30c939374be69a863793b21b567ea9442f2f43e10f4da1217de322266328de36e8c8d22815fb9ee3a0c02f43a4d1753a08ee3f8fbcb335d68444e8dd67fcb897cbb2; C3RD=435e33cbbcf515462f7483757059b33fc37930b4f95aff257748f96b59f56d643a68b089d075a66c59dce2614b8b36aa64df8f2298fce82d80ead5991a5b36713dbf262013f9d4ff1458428c355bb52b3b43ee6a5e16cf9e73965493417934c121461bb787d008b988ff670a239dcbb06b905957fd87648b5443988a8072791c611063bae9237bc38e2c547d4f77c132; ETC=enc%5Fnateon%5Femail=DDBC123BD14DA8D5CEA15DCFEC97AC70&cpinfo=afe148ed6033f90aaec2f8ab608808ce6799b63ab82349963d0f310726c7db6418d489d5a2bda47b7750430bb5d7bff910fc237638702a459de747f9e4854223&NCFLAG=n&CFN=23619c7c5b939a497dbfea0ad05571ab402c12376fb4a8dc522498b428f9239456f2a2ac0f2d40cfe46928ac3928907c5bb328e793f0efa164388e27b5fb539b593e1f50ff39ef08cc0aee807af6a2adeeb3b93f593f845964f44420224c2cd9d725b7148148101767f158e840fcea9b9c6de4d548a9200879968c221abc5603ba5327903f0e47e140297be9f9741967b153869cd350d2e67a5907e6c560a7c81f76da8817b8f147fbb1850b857d34fb7b1ebd17711306d530cc4fce38da2087d2cb3d0e3337f005d0823dfd2d71ad0fa279f0287018f27b4ef2972b0f3ab323f69b541be1dc4f78e99866e99ffd1757761dbb69b364bb3a055a7558143cdb3f; ndrn=|MjIyNjMwMzA=|; RDB=01|39|||KR|; aireToken=; UAKD=3",
        'Accept-Encoding': "gzip, deflate", 'Accept-Language': "ko,en-US;q=0.9,en;q=0.8,ja;q=0.7",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Referer': "http://cy.cyworld.com/home/new/22263030", 'X-Requested-With': "XMLHttpRequest",
        'Connection': "keep-alive", 'cache-control': "no-cache",
        'Postman-Token': "607f3b6b-22fc-4aad-95c5-ed54122c2480"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def data_json_create(data):
    dataParse = json.loads(data)
    return dataParse


def img_download(url, directory, filename, width, height):
    download_url_prefix = 'http://nthumb.cyworld.com//thumb?width=' + str(width) + '&height=' + str(height) + '&url=' + url
    #makedirs(directory)
    mem = urllib.request.urlopen(download_url_prefix).read()
    with open(filename, mode="wb") as f:
        f.write(mem)
        print("저장 되었습니다..!")

def process(last_date, last_id, list_size):
    if list_size != '':
        list_size = '20'
    # cyworld post data를 획득한다.
    data = data_request(last_date, last_id, list_size)
    if data == '':
        print('더이상 다운받을 데이터가 없습니다.')
        return

    jsonData = data_json_create(data.text)
    #print('jsonParsingData = ' + str(jsonData))
    last_date = jsonData['lastdate']
    last_id = ''

    post_list = jsonData['postList']
    for post in post_list:
        last_id = post['identity']
        summary = data_json_create(post['summary'])

        #print(str(summary['type']))
        if summary['media_type'] != 'website':
            try:

                width = summary['width']
                height = summary['height']
                img_url = summary['image']
                '''
                text = summary['text']
                if len(text) >= 0:
                    text = 'noText'
                else:
                    text[:5]
                '''
                print('download img =' + img_url + ' || text = ' + last_id + ' || width = ' + str(width) + ' || height = ' + str(height))
                img_download(img_url, './cyworld-picture', last_id + '.jpg', width, height)
                time.sleep(1)  # 1초 휴식
            except Exception as ex:
                print('error', ex)


    process(last_date, last_id, '20')


if __name__ == "__main__":
    process('', '', '20')