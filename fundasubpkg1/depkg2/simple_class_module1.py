class Class1:
    def __init__(self,a):
        print("Class1 is constructed with a param of :",a)
    def member1(self):
        print("I am the member of ",self)

obj1=Class1(10)
obj1.member1()

obj1=Class1(20)
obj1.member1()