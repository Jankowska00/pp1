class book():
    
    def __init__(self, title, author, pages, current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.open = 0
        
    def open_book(self):
        self.open = 1
        
    def status(self):
        print(f'Tytuł: {self.title}\nAutor: {self.author}\nIlośc stron: {self.pages}\nNumer bieżącej strony: {self.current_page}\n')
        
    def read(self):
        if self.open == 1:
            self.current_page += 1
        else:
            print('Książka jest zamknięta')
        
    def close_book(self):
        self.open = 0