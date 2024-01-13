# Calculation The Duration
Total_Seconds = int(input("Enter the total seconds: \n"))
Hours = Total_Seconds // 3600
Minutes = (Total_Seconds % 3600) // 60
Seconds = (Total_Seconds % 3600) % 60
print(F"The total Duration is {Hours} Hours and {Minutes} Minutes and {Seconds} Seconds.")