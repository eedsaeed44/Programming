
# file = input("Enter file name : ")

# try:
#     handle = open(file)
# except:
#     print("name error ")
#     quit()

# urls = []
# before = 0
# after = 0

# # * One : Replace string
# word_replace = input("enter the the word you want to reblace: ")
# word_put = input("enter the the word you want to put: ")
# for line in handle:
#     line = line.strip()
#     before += 1
#     line.replace(word_replace, word_put)
#     urls.append(line)


# print(line)

# ====================================================================================

my_string = "geeks for geeks "
old_substring = "k"
new_substring = "x"

split_list = my_string.split(old_substring)
new_list = [new_substring if i < len(
    split_list)-1 else '' for i in range(len(split_list)-1)]
new_string = ''.join([split_list[i] + new_list[i]
                     for i in range(len(split_list)-1)] + [split_list[-1]])

print(new_string)






































