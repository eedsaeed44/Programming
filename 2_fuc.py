###*** Code For do two functions ***###
#* One : Replace string
#* Two : Getting just uniqe values

file = input("Enter file name : ")

try:
    handle = open(file)
except:
    print("name error ")
    quit()

urls = []
before = 0
after = 0

#* One : Replace string
word_replace = input("enter the the word you want to reblace: ")
word_put = input("enter the the word you want to put: ")
for line in handle :
    line = line.rstrip()
    before += 1
    line.replace(word_replace, word_put)
    urls.append(line)

#* Two : Getting just uniqe values
uniqe_values = []
for url in urls:
    url = url.rstrip()
    if url in uniqe_values:
        continue
    uniqe_values.append(url)

for n in uniqe_values:
    print(n)
    after += 1

print(line)

print(f"before : {before}")
print(f"after : {after}")