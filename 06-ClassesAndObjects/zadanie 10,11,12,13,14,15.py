class TV():
    
    def __init__(self):
        self.is_on = 0
        self.channel_no = 1
        self.channels = []
        self.volume = 0
        
    def on(self):
        self.is_on = 1
        
    def off(self):
        self.is_on = 0
    
    def showstatus(self):
        if self.is_on == 1:
            print(f'Odbiornik TV jest załączony, kanał {self.channel_no} ({self.channels[(self.channel_no)-1]})\nGłośność {self.volume}')
        else:
            print('Telewizor nie jest załączony')
            
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, channels_list):
        self.channels = channels_list
        
    def show_channels(self):
        for i in range(len(self.channels)):
            print(f'{i+1}. {self.channels[i]}')
            
    def volume_up(self):
        if self.volume<10 and self.volume>= 0:
            self.volume += 1
        else:
            print('Głośność poza zakresem')
        
    def volume_down(self):
        if self.volume<=10 and self.volume>0:
            self.volume -= 1
        else:
            print('Głośność poza zakresem')
        
x = TV()
x.on()
x.set_channels(['TVP', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'TVN7', 'TVN Style'])
x.show_channels()
x.set_channel(1)
x.volume_up()
x.showstatus()
x.set_channel(2)
x.volume_up()
x.showstatus()
x.set_channel(3)
x.volume_up()
x.showstatus()
x.set_channel(4)
x.volume_down()
x.showstatus()
x.set_channel(5)
x.volume_down()
x.showstatus()
x.set_channel(6)
x.volume_up()
x.showstatus()
x.set_channel(7)
x.volume_up()
x.showstatus()

        