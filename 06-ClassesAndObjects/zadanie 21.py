import statistics

class Statystyka():
    
    def __init__(self):
        self.numbers = []
        
    def add(self, number):
        self.numbers.append(number)
        
    def show(self):
        for i in range(len(self.numbers)):
            print(self.numbers[i], end=' ')
        print()
         
    def maximum(self):
        self.numbers.sort()
        return self.numbers[-1]
        
    def minimum(self):
        self.numbers.sort()
        return self.numbers[0]
        
    def mean(self):
        return statistics.mean(self.numbers)
    
    def median(self):
        return statistics.median(self.numbers)
    
    def show_results(self):
        print(f'Minimum: {self.minimum()}\nMaximum: {self.maximum()}\nŚrednia: {self.mean()}\nMediana: {self.median()}')
        
x = Statystyka()
x.add(12)
x.add(37)
x.add(6)
x.add(9)
x.add(17)
x.show()
x.maximum()
x.minimum()
x.mean()
x.median()
x.show_results()
        

        
        
        