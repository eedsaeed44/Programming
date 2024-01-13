#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.
quantity = int(input("Enter the quantity: "))
if quantity*100 > 1000 :
    print(f"the total cost is {quantity*100}")
    print("==================================")
    print("and the end cost is " + str((quantity*100)-(quantity*100)*0.1))
else:
    print(f"Cost is {quantity*100}")

















# print "Enter quantity"
# quantity = input()
# if quantity*100 > 1000:
#   print "Cost is",((quantity*100)-(.1*quantity*100))
# else:
#   print "Cost is",quantity*100