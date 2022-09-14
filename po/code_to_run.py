from op import Librarian, User

Mr_L = Librarian()
Manuel = User(Mr_L)

Mr_L.add_book("Pinocho")
Mr_L.add_book("Disgrace")
Mr_L.add_book("1984")

print("available books:")

Manuel.see_available()

Manuel.borrow_book("1984")

print('available books after user borrowing "1984":')

Manuel.see_available()

Mr_L.remove_book("Disgrace")

print('available books after librarian removing "Disgrace":')

Manuel.see_available()

Manuel.return_book("1984")

print('available books after returning "1984":')

Manuel.see_available()