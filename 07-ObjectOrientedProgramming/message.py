class Message():
    
    def __init__(self):
        self.message = ''
        
    def set_message(self, message):
        self.message = message[0].lower()+message[1:len(message)].upper()+'\nBYE'
   
x = Message()
x.set_message(str(input('Leave a message: ')))