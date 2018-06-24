import random
import urllib.request

def download_img(url):
    name = random.randrange(1,1000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_img("https://mblogthumb-phinf.pstatic.net/MjAxNzA2MjBfNyAg/MDAxNDk3OTE5MzkwODY2.SrJGkcqJfnQD9-2PySA_EWm-xcn82WJGPme0cS7NTa0g.vPsShRY4CHRtBhNwuo6SGy3DxxQvxGh7Ga-pFFDMeE8g.JPEG.jobarajob/0321_%EA%B9%80%ED%98%9C%EC%9D%80.jpg?type=w800")