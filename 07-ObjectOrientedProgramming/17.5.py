class Utwory():
    def __init__(self,wykonawca,tytul,album,rok):
        self.wykonawca = wykonawca
        self.tytul = tytul
        self.album = album
        self.rok = rok
        
    def __str__(self):
        return "Wykonawca: "+ self.wykonawca + "\n" + "Utwór: " + self.tytul + "\n" + "Album: " +self.album +"\n" + "Rok: " + str(self.rok) 

       
utwor1 = Utwory("Pink Floyd","Comfartably Numb","The Wall",1979)
utwor2 = Utwory("The Beatles","A day in the life","Sgt. Pepper Lonely Heart",1966)
utwor3 = Utwory("Pink Floyd","Time","Dark Side of the moon",1973)

print(utwor1)
print(utwor2)
print(utwor3)