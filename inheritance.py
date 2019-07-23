#passing traits from parent to sibling
#getting something from someone else

class Parent():

    def print_last_name(self):
        print("Gupta")

class Child(Parent):
    #the class Child Inherited the method of last_name from Parent Class

    def print_first_name(self):
        print("Sumit")

    def print_last_name(self):
        print("Aggarwal")
        #now child class can overwrite the data from inherited class

''' sumit = Child()
sumit.print_first_name()
sumit.print_last_name()
'''

class Mario():

    def move(self):
        print("I am moving")

class Shrooms():

    def eat_shroom(self):
        print("Now I am Big")

class BigMario(Mario,Shrooms):#multiple inheritance
    pass #if nothing is supposed to be passed

bm = BigMario()
bm.move()
bm.eat_shroom()
