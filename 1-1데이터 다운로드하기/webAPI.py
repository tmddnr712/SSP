# IP확인 API로 접근해서 결과 출력하기
# 모듈 읽어 들이기
import urllib.request

#데이터 읽어들이기
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = urllib.request.urlopen(url)
data = res.read()

#바이너리를 문자열로 변환하기
text = data.decode("utf-8")
print(text)