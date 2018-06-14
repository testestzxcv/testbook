from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.findAll("h")

for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)