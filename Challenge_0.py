#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

#          My solve
print("Enter your salary")
salary = int(input())
print("Enter the duration of service in years")
duration = float(input())
if duration > 5:
    print("your new salary is " + str((salary * 0.05)+ salary))

#====================================================================================================================================


print ("Enter salary")
salary = input()
print ("Enter year of service")
yos = input()
if yos>5:
  print ("Bonus is",.05*salary)
else:
  print ("No bonus")