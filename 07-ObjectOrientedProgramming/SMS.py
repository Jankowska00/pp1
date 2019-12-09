class SMS():
    
    import message
    
    def __init__(self, nadawca, odbiorca):
        self.nr_nadawcy = nadawca
        self.nr_odbiorcy = odbiorca
        
    def send(self):
        return 'Wysyłanie SMS...\n'+'Od:'.ljust(10)+str(self.nr_nadawcy)+'\n'+'Do:'.ljust(10)+str(self.nr_odbiorcy)+'\n'+'Treść:'.ljust(10)+str(message)

    