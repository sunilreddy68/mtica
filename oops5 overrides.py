class Wolf:
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print("grr...")
        

class Dog(Wolf):
    def bark(self):
        print("woof")
    
   

pet1=Dog("Tommy","brown")
pet1.bark()
    
pet2=Wolf("Sheru","white")
pet2.bark()
Dog("abc","xyz").bark()
