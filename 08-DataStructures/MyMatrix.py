class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
            
    @staticmethod
    def creatematrix(y,x):
        return [[0 for x in range(x)] for y in range(y)]
    
    @staticmethod
    def create_unit(x):
        macierz = matrix.create(x,x)
        for i in range(x):
            macierz[i][i]=1
        print(macierz)
        
    @staticmethod
    def fill_random(matrix,m,n):
        import random
        macierz = matrix
        for i in range(len(matrix)-1):
            tab[i]
        
        
matrix.create_unit(5)