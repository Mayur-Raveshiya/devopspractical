from datetime import datetime, timedelta

books = {}

def add_book():
    book = input("Enter Book Name: ")

    if book in books:
        print("Book already exists!")
        return

    books[book] = {
        "issued": False,
        "student": "",
        "issue_date": None,
        "due_date": None
    }

    print("Book added successfully.\n")


def issue_book():
    book = input("Enter Book Name to Issue: ")

    if book not in books:
        print("Book not found.\n")
        return

    if books[book]["issued"]:
        print("Book is already issued.\n")
        return

    student = input("Enter Student Name: ")

    issue_date = datetime.today()
    due_date = issue_date + timedelta(days=14)

    books[book]["issued"] = True
    books[book]["student"] = student
    books[book]["issue_date"] = issue_date
    books[book]["due_date"] = due_date

    print("\nBook Issued Successfully!")
    print("Issue Date :", issue_date.strftime("%d-%m-%Y"))
    print("Due Date   :", due_date.strftime("%d-%m-%Y"))
    print()


def return_book():
    book = input("Enter Book Name to Return: ")

    if book not in books:
        print("Book not found.\n")
        return

    if not books[book]["issued"]:
        print("Book is already available.\n")
        return

    today = datetime.today()
    due = books[book]["due_date"]

    if today > due:
        late_days = (today - due).days
        print(f"Book returned late by {late_days} day(s).")
    else:
        print("Book returned on time.")

    books[book]["issued"] = False
    books[book]["student"] = ""
    books[book]["issue_date"] = None
    books[book]["due_date"] = None

    print("Book Returned Successfully.\n")


def view_books():
    if not books:
        print("No books available.\n")
        return

    print("\n----------- BOOK LIST -----------")

    for name, data in books.items():

        status = "Available"

        if data["issued"]:
            if datetime.today() > data["due_date"]:
                status = "Overdue"
            else:
                status = "Issued"

        print(f"""
Book      : {name}
Status    : {status}
Student   : {data['student']}
Issue Date: {data['issue_date'].strftime('%d-%m-%Y') if data['issue_date'] else '-'}
Due Date  : {data['due_date'].strftime('%d-%m-%Y') if data['due_date'] else '-'}
-----------------------------------
""")

while True:

    print("""
========== BOOK MANAGEMENT ==========
1. Add Book
2. Issue Book
3. Return Book
4. View Books
5. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        view_books()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid choice.\n")