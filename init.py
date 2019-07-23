class Food:
    def __init__(self):#works as constructor; called before calling any method
        print("Food")
    def eat(self):
        print("Eat")
#tuna = Food()
#tuna.eat()


class Enemy:
    def __init__(self, x):
        self.energy = x#values can be passed as initalizers now

    def get_energy(self):
        print(self.energy)

#jason = Enemy(5)
#jason.get_energy()


class Girl:

    gender = "female" #global variable acessed throughout class in class variable

    def __init__(self,name):
        self.name = name #name is unique to each object - inistance variable


r = Girl("Rachel")
s = Girl("Sandy")
print(r.gender)
print(s.gender)
print(s.name)
print(r.name)