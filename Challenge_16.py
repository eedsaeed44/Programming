print("Welcome to place rabbit..\n")
matrix = [['🌲', '🌲', '🌲', '🌲'], ['🌲', '🌲', '🌲', '🌲'], ['🌲', '🌲', '🌲', '🌲'], ['🌲', '🌲', '🌲', '🌲']]
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}")
print("where the place you want rabbit to go..🐇")
input_str = input("enter the raw and the colum : ")

raw = int(input_str[0])
colum = int(input_str[1])

matrix[raw-1][colum-1] = '🐇'
print("\nSuccess!...\n")
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}")
