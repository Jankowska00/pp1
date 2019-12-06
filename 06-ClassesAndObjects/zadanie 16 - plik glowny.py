import ebook

x = ebook.book('Mroczne Materie', 'Phillip Pulman', 958, 500)
x.open_book()
x.status()
for i in range(5):
    x.read()
x.status()
x.close_book()
for i in range(7):
    x.read()

