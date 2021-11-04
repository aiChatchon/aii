class Zoo:
    def __init__(self,name,species,action):
        self.name=name
        self.species=species
        self.action=action
    def introduce(self):
        print("I am a",self.species,"named",self.name)
    def act(self):
        print("I am currently",self.action)
class Entrance():
    def __init__(self,adult,children):
        self.adult_amount= adult
        self.children_amount=children
        self.total= (self.adult_amount*500)+(self.children_amount*200)
        print("The total entry cost is " ,(self.total) ," THB")
    def pay(self):
        print("You paid a total of" ,(self.total)," THB")
        print("Entering the zoo...")
    def leave():
        print("Thank you for your time with us")
        print("Leaving the zoo...")


penguin=Zoo("Toby","penguin","swimming")  
penguin.introduce()
penguin.act()   
lion=Zoo("Max","lion","eating meat")   
lion.introduce()
lion.act()
entering=Entrance(int(input("Adult(s):  ")),int(input("Children(s):  ")))
entering.pay()
Entrance.leave()

