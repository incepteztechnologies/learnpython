#4. Arbitrary (dynamic number of positional arguments) Argument Functions
def final_bill_fun(*args,shipping_charges):
    #Input parameter is considered as tuple type if we prefix * with the param name
    print(type(args))
    print("products amount",args)
    print("shipping Change",shipping_charges)
    total_amt=sum(args)
    final_bill_amt=total_amt-shipping_charges
    return final_bill_amt

total_amt=final_bill_fun(100,200,150,500,shipping_charges=50)
print(total_amt)
total_amt=final_bill_fun(10,40,20,shipping_charges=50)
print(total_amt)

#Module is the place where
#Notebook is to call the functions/instantiate the class /access the variable created under some modules
import dataenggpkg.depython.somemodule
var1=dataenggpkg.depython.somemodule.fun_name(200,100)
var11=dataenggpkg.depython.somemodule.my_complete_fun(200)
print("result",var1)
print("result",var11)
import dataenggpkg.depython.somemodule as sm
var2=sm.fun_name(var1,100)
print(var2)

from dataenggpkg.depython.somemodule import fun_name as fn,fun_name_min as fnm
var3=fn(var1,100)
print(var3)