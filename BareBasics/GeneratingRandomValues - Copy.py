import random
for i in range (3):
    print (random.randint (10, 20))

members = ["John", "Mary", "Bob"]
leader = random.choice (members)
print (leader)


class Dice:
    import random
    def roll (self):
        num1 = random.randint (0, 6)
        num2 = random.randint (0, 6)
        rolled = (num1, num2)
        print (rolled)



dice = Dice ()
dice.roll ()
