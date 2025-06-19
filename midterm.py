def load_books(filename):
    books = {}
    books["001"] = {"title": "The Alchemist", "author": "Paulo Coelho", "copies":3}
    books["002"] = {"title": "1984", "author": "George Orwell", "copies": 2}
    books["003"] = {"title": "To kill a Mockingbird", "author": "Harper Lee", "copies": 1}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 4:
                    book_id, title, author, copies = parts
                    books[book_id] = {
                        "title": title,
                        "author": author,
                        "copies": int(copies)
                    }
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return books

def display_books(books):
    print("\n Available Books:")
    print("{:<5} | {:<30} | {:<20} | {:<6}".format("ID", "Title", "Author", "Copies"))
    print("-" * 72)
    for book_id, info in books.items():
        if info["copies"] > 0:
            print("{:<5} | {:<30} | {:<20} | {:<6}".format(
                book_id, info["title"], info["author"], info["copies"]
            ))

def borrow_books(books, user_name):
    borrowed = []
    while True:
        book_id = input("\nEnter Book ID to borrow (or 'done' to finish): ").strip()
        if book_id.lower() == "done":
            break
        if book_id not in books:
            print(" Book ID not found.")
        elif books[book_id]["copies"] == 0:
            print("No copies left for this book.")
        else:
            books[book_id]["copies"] -= 1
            borrowed.append(book_id)
            print(f"You borrowed '{books[book_id]['title']}'.")

    return borrowed

def log_borrowed_books(filename, user_name, borrowed, books):
    with open(filename, "a") as file:
        for book_id in borrowed:
            book = books[book_id]
            file.write(f"{user_name} borrowed '{book['title']}' by {book['author']}\n")

def borrowing_summary(user_name, borrowed, books):
    print("\nBorrowing Summary")
    print(f"User: {user_name}")
    if not borrowed:
        print("No books were borrowed.")
    else:
        for book_id in borrowed:
            book = books[book_id]
            print(f"- {book['title']} by {book['author']}")

def save_books(filename, books):
    with open(filename, "w") as file:
        for book_id, info in books.items():
            file.write(f"{book_id}, {info['title']}, {info['author']}, {info['copies']}\n")

def main():
    filename = "books.txt"
    log_file = "borrowed.txt"
    
    books = load_books(filename)
    if not books:
        return

    user_name = input("Enter your name: ").strip()
    display_books(books)

    borrowed = borrow_books(books, user_name)
    log_borrowed_books(log_file, user_name, borrowed, books)
    borrowing_summary(user_name, borrowed, books)
    save_books(filename, books)  

if __name__ == "__main__":
    main()
