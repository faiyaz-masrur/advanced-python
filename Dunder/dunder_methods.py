class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"📖 {self.title} ({self.pages} pages)"
    
    def __repr__(self):
        return f"Book(title={self.title!r}, pages={self.pages!r})"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(self.title +' '+ other.title, self.pages + other.pages)
        raise TypeError("Can only add Book to Book")
    
    def __call__(self):
        return f"Book '{self.title}' has {self.pages} pages."

    def __getitem__(self, index):
        return self.title[index]


if __name__ == "__main__":
    book1 = Book("Python Tricks", 300)
    book2 = Book("Fluent Python", 700)

    print(book1())                # Calls __call__
    print(book2())                # Calls __call__
    print(book1)                  # Calls __str__
    print(len(book1))             # Calls __len__
    print(book1 + book2)          # Calls __add__
    print(book1[0:6])             # Calls __getitem__
