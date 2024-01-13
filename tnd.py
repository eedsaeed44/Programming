import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0
bad = 0
bad_urls = []
file = input("Enter file name : ")

try:
    handle = open(file)
except:
    print("name error ")
    quit()

for url in handle:
    try:
        # url = input("Enter URLE : ")
        html = urllib.request.urlopen(url, context=ctx)
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
    except:
        bad+= 1
        bad_urls.extend(url)
        

    for tag in tags:
        try:
            print(tag.get('href', None))
            count += 1
        except:
            bad += 1
            bad_urls.extend(url)
        with open('on.txt', 'a') as f:
            sys.stdout = f
            print(tag.get('href', None))
            sys.stdout = sys.__stdout__


print(f"=> {count} : URLs found")
print(f"=> {bad} : Bad URLs found")
n = str(input("Do you want see bad urls: "))
if n == '' :
    print(bad_urls)
# print(f"The sorce page is: {url}")
