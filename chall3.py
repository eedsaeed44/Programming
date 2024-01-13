names = input("Enter the first and last name of your friends seperated by a comma: ").split(", ")
name_apbbreviated = []
# Eed Saeed, Ali Mazen, Mohamed Saeed, Kamell Nasser, Ziead Hagann
for name in names:
    name_barts = name.split()
    print(name_barts)
    first_name = name_barts[0]
    last_name = name_barts[1]
    first_initial = first_name[0]
    last_initial = last_name[0]

    apbbreviated = first_initial + "." + last_initial + "."
    name_apbbreviated.append(apbbreviated)

for x in name_apbbreviated:
    print(x)

  