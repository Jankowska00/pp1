import message

class Email(message.Message):
    
    def __init__(self, nadawca, odbiorca, temat):
        message.Message.__init__(self)
        self.nadawca = nadawca
        self.odbiorca = odbiorca
        self.temat = temat

    def send(self):
        message.Message.set_message(self,'cześć tu Weronika')
        return 'Wysyłanie emaila...\n'+'Od:'.ljust(8)+self.nadawca+'\n'+'Do:'.ljust(8)+self.odbiorca+'\n'+'Temat:'.ljust(8)+self.temat+'\n'+'Treść:'.ljust(8)+self.message