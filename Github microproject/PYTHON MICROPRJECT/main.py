from library import Library

def main():
    lib = Library()

    # Sample books
    lib.add_book("1984", "George Orwell", "1234567890")
    lib.add_book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    lib.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Books")
        print("5. List Available Books")
        print("6. List Issued Books")
        print("7. Check Overdue Books")
        print("8. Calculate Fine")
        print("9. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            if lib.add_book(title, author, isbn):
                print("Book added.")
            else:
                print("ISBN already exists.")

        elif choice == "2":
            isbn = input("ISBN to issue: ")
            user = input("User name: ")
            days = int(input("Days to issue (default 14): ") or 14)
            if lib.issue_book(isbn, user, days):
                print("Book issued.")
            else:
                print("Book not available or not found.")

        elif choice == "3":
            isbn = input("ISBN to return: ")
            if lib.return_book(isbn):
                print("Book returned.")
            else:
                print("Book not issued or not found.")

        elif choice == "4":
            query = input("Search query: ")
            results = lib.search_books(query)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found.")

        elif choice == "5":
            available = lib.list_available_books()
            if available:
                for book in available:
                    print(book)
            else:
                print("No available books.")

        elif choice == "6":
            issued = lib.list_issued_books()
            if issued:
                for book in issued:
                    print(book)
            else:
                print("No issued books.")

        elif choice == "7":
            overdue = lib.check_overdue()
            if overdue:
                for book in overdue:
                    print(book)
            else:
                print("No overdue books.")

        elif choice == "8":
            isbn = input("ISBN to check fine: ")
            fine = lib.calculate_fine(isbn)
            print(f"Fine: ${fine:.2f}")

        elif choice == "9":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()