class Kontakt():
    
    def __init__(self, nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon
        
class ListaKontaktów():
    
    def __init__(self):
        self.kontakty = []
        
    def add_contact(self, kontakt):
        self.kontakty.append(kontakt)
        
    def show_list(self):
        for x in self.kontakty:
            print(x.nazwa.ljust(15),x.email.ljust(15),x.telefon)
        
x1 = Kontakt('Kowalski Jan', 'jank@onet.pl', '555234000')
x2 = Kontakt('Borek Patrycja', 'bp@o2.pl', '232000199')
x3 = Kontakt('Maj Piotr', 'maj@google.pl', '222999100')
x4 = Kontakt('Adamczyk Anna', 'ada@poczta.pl', '100200300')

l = ListaKontaktów()
l.add_contact(x1)
l.add_contact(x2)
l.add_contact(x3)
l.add_contact(x4)

l.show_list()

