class vulgarFraction():
     
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator
         
    def fraction(self):
        return '{}/{}'.format(self.numerator, self.denumerator)
    
    def reduce(self):
        if self.denumerator % self.numerator == 0 and (self.denumerator / self.numerator) != self.denumerator and self.numerator % self.numerator == 0:
            print('{}/{}'.format(int(self.numerator/self.numerator), int(self.denumerator/self.numerator)))
        elif self.numerator % self.denumerator == 0 and (self.numerator / self.denumerator) != self.numerator and self.denumerator % self.denumerator == 0:
            print('{}/{}'.format(int(self.numerator/self.denumerator), int(self.denumerator/self.denumerator)))
        else:
            print('Ułamek w postaci uproszczonej.')
        
    def show(self):
        print(f'{self.numerator}/{self.denumerator}')
        
x = vulgarFraction(1,12)
x.fraction()
x.show()
x.reduce()





        
    
         
    