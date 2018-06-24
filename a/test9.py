from bs4 import BeautifulSoup
import re
import urllib.request as req

# url = "http://info.finance.naver.com/marketindex/"
# res = req.urlopen(url)
#
# soup = BeautifulSoup(res,'html.parser')
#
# price = soup.select_one("div.head_info > span.value").string
# print(price)

# url = 'https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC#%EC%9E%91%ED%92%88'
# res = req.urlopen(url)
# soup = BeautifulSoup(res,'html.parser')
#
# a_list = soup.select("#mw-content-text > div > ul > li + li")
#
# for a in a_list:
#     name = a.string
#     print("-",name)

# url = "https://ko.wikipedia.org/wiki/%EB%A6%AC%EC%8A%A4%ED%8A%B8"
# res = req.urlopen(url)
# soup = BeautifulSoup(res,"html.parser")
#
# sel = lambda q : print(soup.select_one(q).string)
# # sel("#ca-nstab-main")
# # sel("li#ca-nstab-main")
# # sel("ul > li#ca-nstab-main")
# # sel("ul > #pt-anonuserpage")
# # sel("ul > #pt-anontalk")
# # sel("ul > li#pt-anontalk")
# # sel("li[id='pt-anontalk']")
# # sel("li:nth-of-type(4)")
#
# # print(soup.select_one("#ca-nstab-main").string)
# # print(soup.select("li")[3].string)
# print(soup.find_all("li")[3].string)

# fp = open("fruits-vegetables.html", encoding='utf-8')
# soup = BeautifulSoup(fp, 'html.parser')
#
# print(soup.select_one("li:nth-of-type(3)").string)
# print(soup.select_one("#fr-list > li:nth-of-type(3)").string)
# print(soup.select("#fr-list > li[data-lo='us']")[1].string) # id=fr-list 하위 li[data-lo='us'] 항목중에 2번째 데이터에서 문자추출
# print(soup.select("#fr-list > li.yellow")[0].string)    # id=fr-list 하위 class='yellow' 항목중에 1번째 항목의 데이터에서 문자추출
#
# cond = {"data-lo":"us", "class":"yellow"}   # data-li=us 항목이고 class=yellow 항목 데이터에서 선택
# print(soup.find("li", cond).string) # li 태그중에 cond 데이터에서 문자 추출
#
# print(soup.find(id="fr-list").find("li", cond).string)  # id=fr-list 를 검색한 데이터중에서 li 태그와 cond 데이터에서 문자추출


html = """
<ul>
  <li><a href="hoge.html">hoge</li>
  <li><a href="https://example.com/fuga">fuga*</li>
  <li><a href="https://example.com/foo">foo*</li>
  <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")
li = soup.find_all(href=re.compile(r"^https://"))   # href에 https:// 부분을 검색하여 속성값으로 정의한후 그 정의된 값으로 전체 탐색하여 변수에 저장

for e in li:
    print(e.attrs['href'])  # 속성값이 href에 정의된 속성값을 출력





