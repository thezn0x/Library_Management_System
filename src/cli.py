from library import Library, Book

library = Library()

def main():
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search by Title")
        print("6. Search by Author")
        print("7. Show All Books")
        print("8. Show Available Books")
        print("9. Count Books")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            book = Book(isbn, title, author)
            library.add_new(book)
            
        elif choice == "2":
            isbn = input("Enter ISBN to remove: ").strip()
            library.remove(isbn)

        elif choice == "3":
            title = input("Enter title: ").strip()
            library.search(title)

        elif choice == "4":
            author = input("Enter author: ").strip()
            library.search_by_author(author)

        elif choice == "5":
            isbn = input("Enter ISBN to borrow: ").strip()
            library.borrow(isbn)

        elif choice == "6":
            isbn = input("Enter ISBN to return: ").strip()
            library.returned(isbn)

        elif choice == "7":
            library.show_all()

        elif choice == "8":
            library.show_available()

        elif choice == "9":
            library.count()

        elif choice == "10":
            library.count_borrowed()

        elif choice == "0":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()