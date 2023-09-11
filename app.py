from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choise: """

# user_option = {
#     'a' database.prompt_add_book()
# }

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()

        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("invalid input")
        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the name of the book: ')
    author = input('Enter the author of the book: ')
    database.add_books(name, author)

def list_books():
    show_books()

def show_books():
    books = database.get_all_books()
    for book in books:

        if book['read'] == 'True':
            read = "read"
        else:
            read = "do not read"
        print(f"{book['name']}, by {book['author']} that you {read}")




def prompt_read_book():
    book_name = input("Enter the name of the book you want to read: ")
    database.mark_book_as_read(book_name)

def prompt_delete_book():
    book_name = input("Enter the name of the book you want to delete: ")
    database.delete_book(book_name)


menu()



