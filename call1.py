items_names = []
items_prices = []
print("**** Welcome to ishop calculator ****")
number = int(input("How many items are there in your basket today? "))
if number > 0:
    print("Let's get to counting them....")
    for i in range(1,number):
        item_name = input(f"Please tell me the name of the item {i+1}: ")
        items_names.append(item_name)
        item_price = float(input(f"what is the price of {item_name}\n$"))
        items_prices.append(item_price)
    all_items = input("would you like to see your entire basket itemes? ").lower()
    if all_items == 'yes':
        print(items_names)
    else:
        input("Press Enter TO Excit!")
    all_items_price = input("would you like to see how much it all cost? ").lower()
    if all_items_price == 'yes':
        print("\nBuying these items will cost:")
        print(sum(items_prices))
    else:
        input("Press Enter TO Excit!")
