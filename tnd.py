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

file = input("Enter file name : ")

try:
    handle = open(file)
except:
    print("name error ")
    quit()

for url in handle:
    

    # url = input("Enter URLE : ")
    html = urllib.request.urlopen(url, context=ctx)
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))
        count += 1
        with open('bnb.txt', 'a') as f:
            sys.stdout = f
            print(tag.get('href', None))
            sys.stdout = sys.__stdout__


print(f"count : {count}")
print(f"The sorce page is: {url}")
