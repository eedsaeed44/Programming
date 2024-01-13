import urllib.request
print("File download is starting...")
# path to download
my_path = "E:\Hunting\Download\images"
# image url
url = "	https://wallpapers.com/images/hd/tiger-animal-cave-tbyfqlqrb7bg9vcy.webp"

try:
    urllib.rquest.urlretrieve(url, my_path)
    print("Your file has been downloaded")
except Exception as e:
    print(e)
    pass
finally:
    print("File downloader started and terminated")
