# creat a list of own books
own_books = []
# creat a list of wish books
wish_books = []
input_own_book = input("Enter the name of a book you own: ")
own_books.append(input_own_book)
input_own_book_2 = input("enter the name of another book you own (or press 'Enter' to skip): ")
if input_own_book_2:
    own_books.append(input_own_book_2)
    print("")
    print(f"your library: {own_books}")
    print("")
else:
    print("")
    print(f"Your Liberary:  {own_books}")
    print("")

input_wish_book = input("Enter the name of a book you wish to have in the future: ")
wish_books.append(input_wish_book)
input_wish_book_2 = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")

if input_wish_book_2:
    wish_books.append(input_wish_book_2)
    print("")
    print(f"Your Wishlist: {wish_books}")
    print("")
else:
    print("")

book_get = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if book_get in wish_books:
    wish_books.remove(book_get)
    own_books.append(book_get)
    print("")
    print(f"Update Library:  {own_books}")
    print(f"Update Wishlist:  {wish_books}")
    print("")


book_rem = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")

if book_rem in own_books:
    own_books.remove(book_rem)
    print("")
    print(f"Final Library after Donation:  {own_books}")


print("")

print("========================================================================================================")




