from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

proc_files={}

def enum_links(html, base):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select("link[rel='stylesheet']")
    print("첫 links ===", links)
    links += soup.select("a[href]")
    print("two links === ",links)
    result = []

    for a in links:
        href = a.attrs['href']
        print("href === ", href)
        url = urljoin(base, href)
        print("urljoin === ", url)
        result.append(url)
    return result

def download_file(url):
    o = urlparse(url)
    print("oparser === ",o )
    # print("geturl=== " , o.geturl())
    # print("hostname===",o.hostname)
    savepath = "./" + o.netloc + o.path
    print("savepath === ", savepath)
    if re.search(r"/$", savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    print("savedir === ",savedir)

    if os.path.exists(savepath): return savepath

    if not os.path.exists(savedir):
        print("mkdir=",savedir)
        makedirs(savedir)

    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("다운 실패: ",url)
        return None

def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None:
        print("끝이여!!!")
        return
    if savepath in proc_files: return
    proc_files[savepath] = True
    print("analyze_html", url)

    html = open(savepath, "r", encoding='utf-8').read()
    links = enum_links(html, url)
    print("links 야야 === ", links)

    for link_url in links:
        print("link url ====",link_url)
        print("root_url ====",root_url)
        if link_url.find(root_url) != 0:
            print("링크가 루트 이외의 경로를 나타낸다")
            if not re.search(r".css$", link_url):
                print("link_url이 css가 아니다")
                continue

        if re.search(r".(html|htm)$", link_url):
            analyze_html(link_url, root_url)
            continue
        download_file(link_url)

if __name__ == "__main__":
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)