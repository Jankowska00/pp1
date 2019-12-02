class University():

    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'

    # zachowania obiektu (metody)
    def print_name(self):  
        print(self.name)
        
    # zmiana nazwy uczelni
    def set_name(self, new_name):
        self.name = new_name
        return self.name
        
    # wyświetlanie pełnej nazwy
    def print_fullname(self):
        print(self.fullname)
    
    # zmiana pełnej nazwy
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname
        
# utwórz obiekt klasy University i wyświetl nazwę uczelni
p1 = University()
p1.set_name('AGH')
p1.print_name()
p1.set_fullname(str(input('Wprowadź nazwę: ')))
p1.print_fullname()
