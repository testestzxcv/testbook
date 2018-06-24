import urllib.request
if __name__ == "__main__":
    print("Hello World")
    req = urllib.request.Request("http://www.daum.net")
    data = urllib.request.urlopen(req).read() # data = urllib.requset.urlopen("http://www.daum.net").read()

    print(data)
    f = open("./response.txt", "w")
    f.write(str(data))
    f.close()
