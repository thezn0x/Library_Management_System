from db import get_connection
from psycopg2 import Error

class UnchangableError(Exception):
    pass

class Book:
    def __init__(self, isbn, title, author, available=True):
        self.__isbn = isbn
        self.title = title
        self.author = author
        self.available = available

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        raise UnchangableError("ISBN cannot be changed")

class Library:
    def add_new(self, book):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM books WHERE isbn = %s",(book.isbn,))
                    if cursor.fetchone():
                        print("Book already exists")
                        return False
                    else:
                        cursor.execute(
                            "INSERT INTO books (isbn, title, author, available)VALUES(%s,%s,%s,%s)",
                            (book.isbn, book.title, book.author, book.available)
                            )
                        conn.commit()
                        return True
        except Error as e:
            print(f"Error while adding the book:{e}")  

    def remove(self, isbn):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM books WHERE isbn = %s",(isbn,))
                    result = cursor.fetchone()
                    if result:
                        cursor.execute("DELETE FROM books WHERE isbn = %s",(isbn,))
                        print("Removed Successfully!")
                        conn.commit()
                        return True
                    else:
                        print("Book does not exist")
                        return False
        except Error as e:
            print(f"Error While performing operation: {e}")

    def search(self, title):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM books WHERE title = %s",(title,))
                    result = cursor.fetchone()
                    if result:
                        cursor.execute("SELECT * FROM books WHERE title = %s",(title,))
                        result = cursor.fetchall()
                        for (isbn, title, author, available) in result:
                            print("ISBN:", isbn)
                            print("Title:", title)
                            print("Author:", author)
                            print("Availability:", available)
                            print("----")
                        return True
                    else:
                        print(f"No books with the title \"{title}\" found.")
                        return False
        except Error as e:
            print(f"Error while performing operation: {e}")

    def borrow(self, isbn):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM books WHERE isbn=%s",(isbn,))
                    result=cursor.fetchone()
                    if result:
                        cursor.execute("UPDATE books SET available = %s WHERE isbn = %s",(False,isbn))
                        conn.commit()
                        print("Status Updated Successfully")
                        return True
                    else:
                        print("Book does not exist")
                        return False
        except Error as e:
            print(f"Error While performing operation:{e}")

        

    def returned(self, isbn):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM books WHERE isbn=%s",(isbn,))
                    result=cursor.fetchone()
                    if result:
                        cursor.execute("UPDATE books SET available = %s WHERE isbn = %s",(True,isbn))
                        conn.commit()
                        print("Status Updated Successfully")
                        return True
                    else:
                        print("Book does not exist")
                        return False
        except Error as e:
            print(f"Error while performing operation : {e}")

    def show_all(self):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM books")
                    all_books = cursor.fetchall()
                    for (isbn, title, author, available) in all_books:
                        print("ISBN:", isbn)
                        print("Title:", title)
                        print("Author:", author)
                        print("Availability:", available)
                        print("----")
        except Error as e:
            print(f"Error while performing operation: {e}")

    def show_available(self):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM books WHERE available = %s",(True,))
                    list_of_available = cursor.fetchall()
                    for (isbn, title, author, available) in list_of_available:
                        print("ISBN:", isbn)
                        print("Title:", title)
                        print("Author:", author)
                        print("Availability:", available)
                        print("----")
        except Error as e:
            print(f"Error while performing operation: {e}")

    def count(self):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM books")
                    count = cursor.fetchone()[0]
                    print(f"All books: {count}")
        except Error as e:
            print(f"Error while performing operation: {e}")
    
    def count_borrowed(self):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM books WHERE available = %s",(False,))
                    borrowed_books = cursor.fetchone()[0]
                    print(f"Borrowed Books: {borrowed_books}")
        except Error as e:
            print(f"Error while performing operation: {e}")

    def search_by_author(self, author):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM books WHERE author = %s",(author,))
                    result = cursor.fetchone()
                    if result:
                        cursor.execute("SELECT * FROM books WHERE author = %s",(author,))
                        list_search = cursor.fetchall()
                        for (isbn, title, author, available) in list_search:
                            print("ISBN:", isbn)
                            print("Title:", title)
                            print("Author:", author)
                            print("Availability:", available)
                            print("----")
                    else:
                        print(f"No books with the Author \"{author}\" found.")
        except Error as e:
            print(f"Error while performing operation: {e}")            

