# urllib 읽어 들이기
import urllib.request

# url과 저장 경로 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#다운로
urllib.request.urlretrieve(url, savename)
print("saved")