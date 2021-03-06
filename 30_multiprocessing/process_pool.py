"""
    プロセスプールを用いて、並行処理を行うサンプル.
"""
from datetime import datetime
from urllib.request import urlopen

# 取得対象
urls = [
    "http://www.yoheim.net/image/500.jpg",
    "http://www.yoheim.net/image/501.jpg",
    "http://www.yoheim.net/image/502.jpg",
    "http://www.yoheim.net/image/503.jpg",
    "http://www.yoheim.net/image/504.jpg",
    "http://www.yoheim.net/image/505.jpg",
    "http://www.yoheim.net/image/506.jpg",
    "http://www.yoheim.net/image/507.jpg",
    "http://www.yoheim.net/image/508.jpg",
    "http://www.yoheim.net/image/509.jpg"
]

def get_image(url):
    """
        指定されたURLから画像を取得します.
    """
    print(url)
    with urlopen(url) as res:
        return res.read()

def load_sequencial():
    """
        シーケンシャルに画像を取得します.
    """
    images = []
    for url in urls:
        images.append(get_image(url))

print("シーケンシャル取得")
start = datetime.now()
load_sequencial()
print("実行時間：{}ms".format((datetime.now() - start).microseconds / 1000))


def load_parallel():
    from multiprocessing import Pool
    with Pool(processes=4) as pool:
        images = []
        for image in pool.imap_unordered(get_image, urls):
            images.append(image)

print("----------\nパラレル取得")
start = datetime.now()
load_parallel()
print("実行時間：{}ms".format((datetime.now() - start).microseconds / 1000))
