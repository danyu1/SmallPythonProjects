class Persons:
    def __init__ (self, name):
        self.name = name
    
    #only want to use self with a class
    def talk (self):
        print (f"Hello I'm {self.name}")


guy1 = Persons ("Daniel")
guy1.talk ()
