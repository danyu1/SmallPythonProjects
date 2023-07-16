class Mammal:
    def walk (self):
        print ("walk")
    

#class Dog extends Mammal
class Dog (Mammal):
    def bark (self):
        print ("bark")


class Cat (Mammal):
    def beAnnoying (self):
        print ("Meow")

Loochi = Dog ()
Loochi.walk ()
