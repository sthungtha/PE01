# ============================================================
# 1. BOOK CLASS (OOP)
# ============================================================

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available


# ============================================================
# 2. LIBRARY CLASS (ARRAY + LAMBDAS)
# ============================================================

class Library:
    def __init__(self):
        # Array (list) to store Book objects
        self.books = []

    # Add a book to the array
    def add_book(self, book):
        self.books.append(book)

    # Search by title using lambda
    def search_by_title(self, title):
        return list(filter(lambda b: b.title.lower() == title.lower(), self.books))

    # Search by author using lambda
    def search_by_author(self, author):
        return list(filter(lambda b: b.author.lower() == author.lower(), self.books))

    # Update availability using lambda
    def update_availability(self, title, new_status):
        update = lambda b: setattr(b, "available", new_status) \
            if b.title.lower() == title.lower() else None

        for book in self.books:
            update(book)


# ============================================================
# 3. TESTING THE FUNCTIONALITY
# ============================================================

library = Library()

# Create book instances
book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Animal Farm", "George Orwell", available=False)

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\n========== LIBRARY INVENTORY ==========\n")
for b in library.books:
    print(f"{b.title} by {b.author} — {'Available' if b.available else 'Checked Out'}")

# Search examples
print("\n========== SEARCH RESULTS ==========\n")
print("Search by title '1984':")
for b in library.search_by_title("1984"):
    print(f"- {b.title} by {b.author}")

print("\nSearch by author 'George Orwell':")
for b in library.search_by_author("George Orwell"):
    print(f"- {b.title} by {b.author}")

# Update availability
print("\n========== UPDATING AVAILABILITY ==========\n")
library.update_availability("Animal Farm", True)

print("Updated 'Animal Farm':")
for b in library.search_by_title("Animal Farm"):
    print(f"- {b.title} — {'Available' if b.available else 'Checked Out'}")
