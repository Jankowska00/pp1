import statistics
wynagrodzenia = [21600, 4350, 3920, 5590, 3250, 4010]

srednia = statistics.mean(wynagrodzenia)
print(f'Średnia wynagrodzenia w firmie wynosi: {srednia}')

mediana = statistics.median(wynagrodzenia)
print(f'Mediana wynosi: {mediana}')

odchylenieStandardowe = statistics.stdev(wynagrodzenia)
print(f'Odchylenie standardowe wynosi: {odchylenieStandardowe}')