class Book:
    def __init__(self, title, author, publication_year, genre, pages):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.pages = pages

    def get_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")

    def read_pages(self, pages_read):
        if pages_read > self.pages:
            print("You can't read more pages than the book has!")
        else:
            self.pages -= pages_read
            print(f"You read {pages_read} pages. There are {self.pages} pages left.")
