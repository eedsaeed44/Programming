from bs4 import BeautifulSoup
import re
count = 0
with open("index.html", 'r') as f:
    doc = BeautifulSoup(f, features="html.parser")

tags = doc.find_all("a")

for tag in tags :
    count += 1
    print(tag)
print(f"Count: {count}")