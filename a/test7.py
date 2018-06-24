from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

request = Request('http://cu.bgfretail.com/store/list.do?category=store')
resp = urlopen(request)
html = resp.read().decode('utf-8')

# print(html)

bs = BeautifulSoup(html, 'html.parser')
print(bs)