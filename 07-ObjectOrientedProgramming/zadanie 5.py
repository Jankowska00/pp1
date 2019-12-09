class utwór():
    
    def __init__(self, wykonawca, tytuł, album, rok):
        self.wykonawca = wykonawca
        self.tytuł = tytuł
        self.album = album
        self.rok = rok
        
    def __str__(self):
        return "Wykonawca: ".ljust(11)+self.wykonawca+'\n'+"Utwór: ".ljust(11)+self.tytuł+'\n'+'Album: '.ljust(11)+self.album+'\n'+'Rok: '.ljust(11)+self.rok+'\n'

x1 = utwór('Dawid Podsiadło', 'Nie ma fal', 'Małomiasteczkowy', '2018')
print(x1)
x2 = utwór('Madonna', 'Isaac', 'Confessions on a Dance Floor', '2005')
print(x2)
x3 = utwór('Bovska', 'Mocno mocno', 'Kęsy', '2018')
print(x3)
x4 = utwór('Ciara', 'Level up', 'Level up', '2018')
print(x4)
        