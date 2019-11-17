import re
tekst = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
samogloska = str(input('Podaj samogłoskę: '))
def ile(samogloska, tekst):
    samogloski = re.findall(samogloska, tekst)
    ilosc = len(samogloski)
    print(f'Ilość samogłoski {samogloska} w tekście: {ilosc}')
  
ile(samogloska, tekst)