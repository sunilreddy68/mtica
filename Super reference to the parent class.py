class A:
    def first_method(self):
        print("method of class A..")
class B(A):
    def second_method(self):
        print("method of class b..")
        super().first_method()
ob=B()
ob.first_method()

