print("**** Welcome to the multiplication table ****")
number = int(input("Entre a number: "))
print(f"Multiplication table for {number}:\n")
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")