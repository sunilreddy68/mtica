class Animal:
    def __init__(self,name,color):
        self.color=color
        self.name=name
class Cat(Animal):
    def mew(self):
        print("cat meows")
##class Dog(Animal):
##    def bark(self):
##        print("woof")
##  
if __name__=="__main__":
    #pet1=Dog("tommy","brown")
    pet2=Cat("Sheru","white")
    #pet1.bark()
    pet2.mew()
    #print(pet1.name)
    print(pet2.name)
    
