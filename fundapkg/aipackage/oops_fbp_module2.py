#Func Based Programming
name='irfan'#variable
def fun1():#function
    return 'fun1 returning'
def fun2():
    return 'fun2 returning'

class FatherHouse:#syntax line1
    def son1(self):#method (member) (A function can be called as a method when it has first param mandatory)
        print('kader.irfan')
        print(self)
        return 'fun1 returning'
    def daughter(xyz,param1,param2):#syntax line2 (self)
        print(xyz)
        return f'fun2 returning {param1} and {param2}'

hand_memory_object1 = FatherHouse() # () is a constructor (doubleclick ())
print(hand_memory_object1.son1())
print(hand_memory_object1.daughter(10,20))

#Four core concepts of OOPS
#1. Class -
#2. Methods (members), self argument
#3. Constructor - Class() ( () that instantiate/construct the class in memory)
#4. Object - Variable that holds the class program in memory

import pandas.io.excel as pio
#FBP
pio.read_excel("E:\\pkg1\\subpkg1\\module2_class.xlsx")

#OOPs
obj1=pio.ExcelFile("E:\\pkg1\\subpkg1\\module2_class.xlsx")
print(obj1.close())#method
#obj1.close()

lst=list([1,2,3,4])
len(lst)#function
lst.__len__()#method
