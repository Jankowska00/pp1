class airplane():
    
    def __init__(self, number):
        self.number = number
        self.height = 0
        
    def start(self, height):
        if height<=2000 and height>=1000:
            self.height += height
        else:
            print('Samolot nie może wystartować na taką wysokość')
        
    def fly_up(self, up):
        if up<=11000 and up >= 300:
            self.height = up
        else:
            print('Komunikat ostrzegawczy!')
        
    def fly_down(self, down):
        if down<=11000 and down >=300:
            self.height = down
        else:
            print('Komunikakat ostrzegawczy!')
            
    def landing(self):
        if self.height<500:
            self.height=0
        else:
            print('Zbyt duża wysokość do lądowania. Obniż lot.')
            
    def status(self):
        print(f'Tu {self.number}, moja wysokość lotu to {self.height}m')
        
x=airplane('LOT881')
x.start(1020)
x.status()
x.fly_up(8900)
x.status()
x.fly_down(200)
x.status()
x.landing()
x.status()
            
    
        
        
        