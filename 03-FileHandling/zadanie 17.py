tekst = 'To be, or not to be, that is the question'
import re
samogloski = re.findall('[aeiouy]', tekst)
suma = len(samogloski)
print(suma)