class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee:", Employee.empCount)
    def displayEmployee(self):
       print("Name:",self.name,",salary:", self.salary)
emp1=Employee("MP",87000)
emp1.displayEmployee()
emp1.salary=77000
emp1.experience=3
emp1.displayEmployee()
emp1.name='Madhu'
emp1.displayEmployee
print(emp1.experience)

emp1.displayEmployee()
