class student():
    
    uczelnia = 'UEK Kraków'
    licznik = 100000

    def __init__(self, imię, nazwisko, kierunek):
        self.imię = imię
        self.nazwisko = nazwisko
        self.nr_albumu = student.licznik
        self.kierunek = kierunek
        student.licznik += 1
        
    def __str__(self):
        return self.imię+' '+self.nazwisko.upper()+' '+'('+str(student.licznik)+')'+', '+self.kierunek+', '+student.uczelnia
    
x1 = student('Wacław', 'Potocki', 'Informatyka stosowana')
print(x1)
x2 = student('Weronika', 'Jankowska', 'Ekonomia')
print(x2)
x3 = student('Bartosz', 'Małocha', 'Zarządzanie')
print(x3)
x4 = student('Wiktoria', 'Szaradowska', 'Marketing')
print(x4)
        

        
        