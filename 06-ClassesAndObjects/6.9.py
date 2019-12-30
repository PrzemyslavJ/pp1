class University():
    def __init__(self):
        self.name = 'UEK'
        self.fullname = 'Uniwersytet ekonomiczny w Krakowie'
    
    def print_name(self):
        print(self.name)
    
    def set_name(self,new_name):
        self.name = new_name
        
    def print_fullname(self):
        print(self.fullname)
        
    def set_fullname(self,new_name):
        self.fullname = new_name
        
Uni = University()
Uni.set_name('AGH')
Uni.print_name()
Uni.print_fullname()
Uni.set_fullname('Akademia Górniczo - Hutnicza')
Uni.print_fullname()

