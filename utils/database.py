
def add_books(name, author,read=False):
    with open('books.txt', 'a') as b:
        b.writelines(f"{name},{author},{read}\n")
    # books.append({"name": name, "author": author, "read": False})

def get_all_books():
    with open('books.txt', 'r') as b:
        lines = [book.strip().split(',') for book in  b.readlines()]
        return [
            {'name': line[0], 'author': line[1], 'read': line[2]} for line in lines
        ]


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
        _save_books(books)
def _save_books(books):
    with open('books.txt', 'w') as file:
        for book in books:
            read = "read" if book['read'] == True else "do not read"
            file.write(f"{book['name']}, {book['author']}, {book['read']}\n")



def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_books(books)


