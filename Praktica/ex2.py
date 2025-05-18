from book import Book
library = [
    Book("1984", "George Orwell"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("The Great Gatsby", "F. Scott Fitzgerald")
]

# Печатаем библиотеку
for book in library:
    print(f"{book.title} - {book.author}")