is_egyption = input("Are you Egyption? type 'yes' or 'no' ").lower()

if is_egyption == "yes":
    print("Good, that is the first step")

    is_18 = input("Are above 18 ? type 'yes' or 'no' ").lower()

    if is_18 == "yes" :
        print("You can Have an ID")
    else:
        print("Sorry, You have to be 18 or older")
        print("Please try again when you are 18")
else:
    print("Sorry, an Egyption ID is give only to Egyptions")