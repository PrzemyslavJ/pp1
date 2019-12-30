class Students():
    
    Nr = 100000
    Uczelnia = "UEK"
    
    def __init__(self,imie,nazwisko,kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nralbumu = Students.Nr + 1
        self.kierunek = kierunek
        self.uczelnia = "UEK"
        Students.Nr = self.nralbumu
    
    def PrintStudent(self):
        print("Imie: {} Nazwisko: {}, Nr albumu {}, kierunek {}, Uczelnia {}".format(self.imie,self.nazwisko.self.nralbumu,self.kierunek,Students.uczelnia))
        
student1 = Students("Przemek","Jaworski","Informatyka stosowana")
student2 = Students("Szymon","Jendrzejek","Mechanika")
student2 = Students("Jan","Kowalski","Ekonomia")
student1.PrintStudent()
student2.PrintStudent()
student3.PrintStudent()