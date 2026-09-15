#1. Indend based prog
word="hello"

for chr in word:
    print(chr)
    if word=='hello':
        print("salutaion")

#2. Comments: (description or dead codes)
#single line comment
'''multi line comments'''
"""multi line comments"""

#3. Quotes usage: ',",''',"""
name='Inceptez Tech'
name="Inceptez Tech"
name='''Inceptez Tech'''
name="""Inceptez Tech"""

#4. Variables & Values (Python)


#Characteristics of variables (python):
#1. Dynamic Inference - Static Defined(Java) Integer aspirant_cnt=103;
aspirants_cnt=103
print("Dynamic inference of the type based on the values assigned",type(aspirants_cnt))
aspirants_cnt='Hundred & Four'
print("Dynamic inference of the type based on the values assigned",type(aspirants_cnt))

#2. Dynamic Typed - Static Typed (Java)
aspirants_cnt=103
print(type(aspirants_cnt))
aspirants_cnt='Hundred & Four'
print('In python we can change the type of a variable Dynamically in the later part of the program',type(aspirants_cnt))

#3. Strongly Typed - Weakly Typed
mentor_name='Irfan'
print(type(mentor_name))
aspirants_cnt=103
print(type(aspirants_cnt))
#name_and_cnt=mentor_name+aspirants_cnt#This code will not work
#print("This will not execute",name_and_cnt)


#E. Datatypes in Python
#1. Simple Types - str, number(int,float,complex number)
#String Type: Indexed Sequenced

#Below string is indexed for eg: I=0, r=1, f=2....
name:str="Irfan"#:str is just a hint, it is not a type definition
print(type(name))#To understand the type of a variable, we use type function
#How to evaluate a given variable is of an expected type? isinstance()
print(isinstance(name,str))

#str - String is a sequence type (a type than can be looped/iterated using index).
print(name[0])#print first element of the string
for idx in name:
    print(idx)#print the each character in sequence

#number type: Not a sequnce type
#int - Integer type will hold whole number without decimal., Integer is not sequence type
age=44
print(type(age))
print(isinstance(age,int))

#float - Float type will hold decimal values
height=5.11
print(type(height))
print(isinstance(height,float))

#2. Collection/Complex Types
#3. Misc Types: bytes, bool, None
#boolean type : True/False