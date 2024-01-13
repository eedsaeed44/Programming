print("            📚📖✨📚📖✨📚📖✨")
print("welcome to the library ")
print("What is subject you search in ?")
subject_choice = input("Please chose one of these choices: 'Psychology, sociology, mathematics, physics, biology'\n").lower()
if subject_choice == "psychology":
    print("Great! Choice, There are alot of Psychology books: ")
    print("01) The Happiness Hypothesis: Finding Modern Truth in Ancient Wisdom by Jonathan Haidt")
    print("02) Influence : The Psychology of Persuasion (New and Expanded) by PhD Robert B. Cialdini")
    book_choice = input("Choose the book number! \n")
    if book_choice == "01" or "1" :
        print("The book you chose is The Happiness Hypothesis: Finding Modern Truth in Ancient Wisdom by Jonathan Haidt")
        print("Do you want a hard copy or a soft copy? ")
        kind_choice = input("").lower()
        if kind_choice == "a hard copy" or "hard copy" or "hard":
            print("Okay, you chose The Happiness Hypothesis book as a hard copy")
            # hard_copy_price_1 = 30
            # print("Do you have a library subscription?")
            # subscriptiont = input("").lower()
            # if subscriptiont == "yes":
            #     print("Ok,What type of subscription do you have? Yearly or biannual ")
            #     kind_subscrib = input("").lower()
            #     if kind_subscrib == "annual" or "yearly":
            #         print("Nice, You will take 30%  discount on your purchases")
            #         print("The book you chose is The Happiness Hypothesis: Finding Modern Truth in Ancient Wisdom by Jonathan Haidt")
            #         print(f"The base price is : {hard_copy_price_1}$ ")
            #         print(f" And The price after discount is : { hard_copy_price_1 - (hard_copy_price_1 * 0.3)}$ ")
            #         print("Have a nice day 😊😊😊😊")

            #     elif kind_subscrib == "biannual":
            #         print("Nice, You will take 15%  discount on your purchases")
            #         print("The book you chose is The Happiness Hypothesis: Finding Modern Truth in Ancient Wisdom by Jonathan Haidt")
            #         print(f"The base price is : {hard_copy_price_1}$ ")
            #         print(f" And The price after discount is : { hard_copy_price_1 - (hard_copy_price_1 * 0.15)}$ ")
            #         print("Have a nice day 😊😊😊😊")
            #     else:
            #        print("Invalid choice! Type Yearly or biannual only 🤔 🤔 🤔 ") 

            # elif subscriptiont == "no":
            #     print("Sorry, you can not get a Discount on purchases")


            # else:
            #      print("Invalid choice!   Type yes or no only 🤔 🤔 🤔 ")

        elif kind_choice == "a soft copy" or "soft copy" or "soft":
            print("Okay, you chose The Happiness Hypothesis book as a soft copy")
            soft_copy_price_1 = 25
            print("Do you have a library subscription?")
            subscriptiont = input("").lower()
            if subscriptiont == "yes":
                print("Ok,What type of subscription do you have? Yearly or biannual ")
                kind_subscrib = input("").lower()
                if kind_subscrib == "annual" or "yearly":
                    print("Nice, You will take 30% discount on your purchases")
                    print(f"The base price is : {soft_copy_price_1}$ ")
                    print(f" And The price after discount is : { soft_copy_price_1 - (soft_copy_price_1 * 0.3)}$ ")
                    print("Have a nice day 😊😊😊😊")

                elif kind_subscrib == "biannual":
                    print("Nice, You will take 15%  discount on your purchases")
                    print(f"The base price is : {soft_copy_price_1}$ ")
                    print(f" And The price after discount is : { soft_copy_price_1 - (soft_copy_price_1 * 0.15)}$ ")
                    print("Have a nice day 😊😊😊😊")
                else:
                   print("Invalid choice! Type Yearly or biannual only 🤔 🤔 🤔 ") 

            elif subscriptiont == "no":
                print("Sorry, you can not get a Discount on purchases")


            else:
                 print("Invalid choice!   Type yes or no only 🤔 🤔 🤔 ")         

        else:
            print("Invalid choice! Type hard or soft only 🤔 🤔 🤔 ") 

   
else:
    print("Invalid choice! 🤔 🤔 🤔 ")