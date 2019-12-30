class TV():
    def __init__(self):
        self.is_on = False
        self.program = 1
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if(self.is_on == True):
            print("Telewizor jest załączony, kanał nr. ",self.program)
        if(self.is_on == False):
            print("Telewizor jest wyłączony")

Ob = TV()
Ob.show_status()
Ob.on()
Ob.show_status()
Ob.off()
Ob.show_status()
        
    