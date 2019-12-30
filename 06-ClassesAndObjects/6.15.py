class TV():
    def __init__(self):
        self.is_on = False
        self.program = 1
        self.channels = []
        self.Volume = 0

    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if(self.is_on == True):
            print("Telewizor jest załączony, kanał nr. ",self.program, end=' ')
            if(len(self.channels) > 0):
                print("Nazwa programu: ", self.channels[self.program-1])
        if(self.is_on == False):
            print("Telewizor jest wyłączony", end =' ')
        
        print("poziom głośności: ",self.Volume)
    
    def set_channel(self,new_channel_no):
        if  new_channel_no <= len(self.channels):
            self.program = new_channel_no
        else:
           print("Program poza zakresem")
        
    def set_channels(self,channel_list):
        self.channels = channel_list
        
    def show_channels(self):
        print("Lista kanałów:",end =' ')
        print(list(self.channels))
        
    def VolumeExtend(self):
        if(self.Volume <10):
            self.Volume+=1
        else:
            print("Osiągnięto Max poziomu głosnośći !")
            
    def VolumeRegress(self):
        if(self.Volume >=0):
            self.Volume-=1
        else:
            print("Osiągnięto Min poziomu głośnosci !")
            
        
    

Ob = TV()
Ob.show_status()
Ob.on()
Ob.show_status()
Ob.show_channels()
kanaly = ["TVP1","TVP2","Polsat","TVN", "Flimbox","Tvn24","PolsatNews"]
Ob.set_channels(kanaly)
Ob.show_channels()
Ob.show_status()
Nr = int(input("Zmień kanał: "))
Ob.set_channel(Nr)
Ob.show_status()
Ob.VolumeExtend()
Ob.VolumeExtend()
Ob.VolumeRegress()
Ob.show_status()
        
    