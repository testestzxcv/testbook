import urllib.request

# url = "http://api.aoikujira.com/ip/ini"
url = "http://www.naver.com"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)