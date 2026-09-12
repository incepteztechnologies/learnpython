#Indendation - alignment based prog/block based prog
#Block management of python is through indendatation & indentation is mandatory in python.

box='xyz' #interpreter1



if box=='pen': #block of code #interpreter2
    print("it is a stationary box")#interpreter2
    print("i can use this box to keep pencil also")#interpreter2
print("i can use this box to keep rubber also")#out of if block
print("i can use this box to keep eraser also")


#Indendation plays an important role of a program? try keeping last print with or without 4 spaces?
aspirants_list=['Gopinath','Karthikeyan','Saravanan','Viji']
for aspirants in aspirants_list:
    print("good morning ",aspirants)
    print("good morning rest of all aspirants")

''' dead code
else:
    print("some other box")
'''

#Comments:
#2 notations for comments: 1. # for single line , 2. ''' ''' or """ """ for multi lines
#2 purposes:
#1. for providing some descriptions
#2. for creating dead codes
#We are using the below block of code for saluting/greeting our aspirants,
# greeting 4 aspirants individually and the rest is group

aspirants_list=['Gopinath','Karthikeyan','Saravanan','Viji'] #this line holds list of values in a variable of type list
for aspirants in aspirants_list:
    print("good morning ",aspirants)
    print("good morning rest of all aspirants")
#End of salutation

#Usage of quotes (single, double, triple)
#name='this is Irfan's mobile' #Throw error
name='this is Irfan\'s mobile'
print(name)
name="this is Irfan's mobile"#If this text is not provided with escape sequence \
print(name)
name='this is Irfan "mobile"'#Single encloses double quotes & vice versa
print(name)
name='''this is Irfan's "mobile" '''
name="""this is Irfan's "mobile" """
print(name)
#Below is bit complex to manage multi lines
statements=("hello team\n"
            "good morning\n"
            "how are you\n")
#We can easily manage multilines using ''' or """
statements=("""hello team
good morning
how are you""")
print(statements)

#Variables & Naming convention
#Python - dynamic inference, dynamic typed & strongly typed lang
#dyn inference
a=10#assigning int type to variable a, py is inferring the type from the value
print(type(a))

#dyn typed (Duck type language)
a=10#type can be changed later
print(type(a))#int
a='ten'
print(type(a))#str

#Strongly typed - operation between two different type (of different hierarchy) is not possible
a=10#int (number family)
b='twenty'#str (string family)
print(a+b)#Fail

#Scala/Java are opposite of python - statically defined, statically typed & weakly typed lang
#String a='ten' #Statically defined
#a=10 #Not possible (Statically typed)
#String a='ten'
#Integer b=10
#System.out.println(a+b) # This works in java, because it is weakly typed language



















