class bankAccount():
    
    def __init__(self, number):
        self.nr = str(number)
        self.money = 0
        
    def pay(self, new_money):
        self.money += new_money
        
    def withdraw(self, amount_money):
        if amount_money < self.money:
            self.money -= amount_money
        else:
            print('Niewystarczająca ilość środków na rachunku.')
            
    def show(self):
        print('Rachunek nr: ', end='')
        print(self.nr[:2] ,self.nr[:4], self.nr[:4], self.nr[:4], self.nr[:4], self.nr[:4], self.nr[:4])
        print(f'Saldo: {float(self.money)} zł')
        
x = bankAccount(12345655559090111100007722)
x.show()
x.pay(25.30)
x.show()
x.withdraw(31.70)
x.show()
x.pay(14)
x.show()
        