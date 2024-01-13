list = [['apples', 'bananas'], ['milk', 'water']]
input("Press enter to change the content .....")


list[0].insert(0, 'orange')
list[0].append('kiwis')
list[1].insert(0, 'coffee')
list[1].remove('water')
list[1].append('tea')
list.append([1, 2, 3])
print("Here is the updated basket: ")
print(list)
