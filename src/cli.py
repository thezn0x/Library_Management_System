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
        elif choice == "0":
            break
        # other options...
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
