"""
Library Management System: The user can do many things in the 
Library Management system, the user can borrow a book, 
return a book and display available books. 
The Librarian should be able to upload a list of books, 
and modify such list if a book is lost or damaged
"""

class Librarian:
    def __init__(self) -> None:
        self.books_available = []

    """
    El librarian va a poder añadir o quitar un libro de la lista de libros
    """

    def add_book(self, book: str) -> None:
        self.books_available.append(book)
        """
        Añade un libro a la lista de la biblioteca
        """

    def remove_book(self, book: str) -> None:
        self.books_available.remove(book)
        """
        Quita un libro de la lista de la biblioteca
        """

class User:
    def __init__(self, librarian: Librarian) -> None:
        self.borrowed_books = []
        self.librarian = librarian
    """
    El usuario puede tomar un libro de la lista de la biblioteca 
    y añadirlo a la lista de libros que ha pedido prestado, 
    como devolver un libro de esta lista a aquella de la biblioteca
    """
    def borrow_book(self, book: str) -> None:
        if book in self.librarian.books_available:
            self.borrowed_books.append(book)
            self.librarian.books_available.remove(book)
        """
        Busca el libro en la lista ofrecida por el Librarian y lo añade
        a la lista de libros tomados prestados por el usuario
        """

    def return_book(self, book: str) -> None:
        if book in self.borrowed_books:
            self.librarian.books_available.append(book)
            self.borrowed_books.remove(book)

        """
        Busca el libro en la lista de libros pedidos por el usuario
        y lo devuelve a la lista de libros de la biblioteca
        """

    def see_available(self) -> None:
        for book in self.librarian.books_available:
            print(book)

        """
        Muestra la lista de libros disponibles ofrecidos por la biblioteca
        """




