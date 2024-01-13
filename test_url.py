import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sys
file = input("enter the file name ")
handle = open(file)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
for n in handle:
    url = n
    try:
        # url = input("Enter URLE : ")
        html = urllib.request.urlopen(url, context=ctx)
        soup = BeautifulSoup(html, 'html.parser')
        count = 0
        tags = soup('a')
        for tag in tags:
            print(tag.get('href', None))
            count += 1
            with open('all.txt', 'a') as f:
                sys.stdout = f
                print(tag.get('href', None))
                sys.stdout = sys.__stdout__
    except:
        print("error==============================================================error")
            


# print(f"count : {count}")
# print(f"The sorce page is: {url}")
