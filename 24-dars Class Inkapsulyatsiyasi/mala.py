class Book:
    def __init__(self):
        self.__title = ""
        self.__author = ""
        self.__pages = 0

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages

    def get_pages(self):
        return self.__pages

# Sinov
book1 = Book()
book1.set_title("Oq kema")
book1.set_author("Chingiz Aytmatov")
# book1.set_pages(150)

print("Kitob nomi:", book1.get_title())
print("Muallifi:", book1.get_author())
print("Sahifalar soni:", book1.get_pages())
