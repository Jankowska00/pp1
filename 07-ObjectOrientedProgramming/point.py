class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            print('Points are equal.')
        else:
            print('Points are different.')
            
        
    def __str__(self):
        return f'P({self.x},{self.y})'
