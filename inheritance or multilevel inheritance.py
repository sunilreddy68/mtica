class A:
    def first_method(self):
        print("method of class A..")
class B(A):
    def second_method(self):
        print("method of class b..")


class C(B):
    def third_method(self):
        print("method of class c..")
if __name__=="__main__":
    ob=C()
    ob.first_method()
    ob.second_method()
    ob.third_method()
    #c().third_method()
#circular inheritance is not possible.
