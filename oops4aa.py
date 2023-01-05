class Animal:
    def __init__(self,name,color):
        self.color=color
        self.name=name
class Cat(Animal):
    def mew(self):
        print("Cat mews")
class Dog(Animal):
    
    def bark1(self):
        print("Dog barks")
        
if __name__=="__main__":
    pet1=Dog("Tommy","brown")
    pet1.bark1()
    print(pet1.name," is of color ",pet1.color)
    pet2=Cat("Sheru","white")
    pet2.mew()
    print(pet2.name," is of color ",pet2.color)
