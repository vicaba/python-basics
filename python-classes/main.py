from book import Book

def main():
    my_book = Book('1984', 'George Orwell', 1949, 'Dystopian Fiction', 328)
    my_book.get_info()
    my_book.read_pages(50)
    my_book.get_info()

if __name__ == "__main__":
    main()