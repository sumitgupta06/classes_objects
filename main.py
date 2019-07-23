class Enemy:#creates a class name enemy
    life = 3#life variable is a global class variable

    def attack(self): #attack is a method/function od class enemy, self is used to call the variables of class in use
        print("ouch!")
        self.life -= 1 #acessing the variable in the class using self

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + "life left")

#in order to acess a function inside the class - we need to create an object of the class
#every object is independent to each other acting as copy of the class


enemy1 = Enemy()

enemy1.attack()
enemy1.checkLife()
