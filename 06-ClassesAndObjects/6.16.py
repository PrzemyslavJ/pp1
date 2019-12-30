class Book():
    def __init__(self,tytul,autor,liczbastron):
        self.tytul = tytul
        self.autor = autor
        self.liczbastron = liczbastron
        self.open = False
        self.nrstrony = 0
    
    def Open(self):
        self.open = True
        self.nrstrony = 1
        
    def Close(self):
        self.open = False
        self.nrstrony = 0
        
    def Show_status(self):
        print("Tytuł książki: {} Autor: {} Liczba Stron: {}, Numer biężącej strony: {}".format(self.tytul,self.autor,self.liczbastron,self.nrstrony))
        
    def Read(self):
        if(self.nrstrony<self.liczbastron and self.open == True):
            self.nrstrony+=1
        else:
            print("Książka zamknięta lub poza zakresem")
        
Ks = Book("1984","Goerge Orwell",350)
Ks.Open()
Ks.Show_status()
Ks.Read()
Ks.Read()
Ks.Read()
Ks.Show_status()
Ks.Close()
Ks.Read()

