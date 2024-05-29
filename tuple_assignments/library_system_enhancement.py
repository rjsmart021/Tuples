from typing import Tuple

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

books_inserted = set([book_name for book_name, author in library])


def insert_book(book_details: Tuple[str, str]):
    book_name, author = book_details

    if book_name not in books_inserted:
        library.append(book_details)
        print(f"Book {book_details} inserted successfully")
        books_inserted.add(book_name)

    else:
        print(f"Book already existed in list : {library}")


def get_library_books():
    return library


user_input = ""

while True:
    book_name = input("Enter Book name to insert (Enter 'finish' or 'done' to exit): ")
    if book_name.lower() in ['finish', 'done']:
        break
    author_name = input("Enter Author name to insert (Enter 'finish' or 'done' to exit): ")
    if author_name.lower() in ['finish', 'done']:
        break
    insert_book((book_name.strip(), author_name.strip()))

print(get_library_books())
