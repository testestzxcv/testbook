import urllib.request

url = "http://cimg.gabangpop.co.kr/images/goods_img/20161215/396372/396372_a_280.jpg"
savename = "test2.png"

mem = urllib.request.urlopen(url).read()
mem2 = mem

with open(savename, mode='wb') as f:
    f.write(mem2)
    print("저장되었습니다...!")

