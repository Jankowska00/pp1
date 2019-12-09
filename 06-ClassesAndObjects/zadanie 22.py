import random

class Thermometer():
    
    def __init__(self):
        self.is_on = 0
        self.temperature = 0
        
    def measure(self):
        self.temperature = float(random.randint(34, 42))
        
    def on(self):
        self.is_on = 1
        
    def off(self):
        self.is_on = 0
        
    def showTemperature(self):
        if self.is_on ==1:
            if self.temperature <37:
                print(f'Zmierzona temperatura: {self.temperature}C')
            elif self.temperature>=37 and self.temperature<41:
                print(f'Zmierzona temperatura: {self.temperature}C (gorączka)')
            else:
                print('Stan zagrożenia życia!!!')
            
x = Thermometer()
x.on()
x.measure()
x.showTemperature()
x.off()
        