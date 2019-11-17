jezyki = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android'] 
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
def rysujWykres(jezyki,wartosci):
    for i in range(len(jezyki)):
        print(jezyki[i],':', '#'*wartosci[i])
        
rysujWykres(jezyki,wartosci)
    