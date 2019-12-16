import email
import message
import SMS

e = email.Email('weri@live.co.uk', 'bart@onet.pl', 'Powitanie')
m = message.Message()
print(e.send())
s = SMS.SMS(603256052, 737935028)
print(s.send())




