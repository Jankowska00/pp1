def suma(N):
    if N == 1:
        return N
    elif N >1:
        return (N + suma(N-1))
    
print(suma(500))
