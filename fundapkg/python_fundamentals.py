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


#12/09/2026 learnings:
#Python Data Types
#Simple, Complex/Collection & Misc types.
#Simple type
#String type: INDEXED SEQUENCED, this type is ITERABLE(LOOPING), Immutable(non updatable)
my_name="Mohamed Irfan"
print(my_name)
print(type(my_name))
#Indexed Sequenced?
#internally  0123456789101112
my_name=    "mohamed irfan"
print(my_name[0])
print(my_name[1])
print(my_name[-1])
print(my_name.capitalize())

#Iterable (loopable)
for letter in my_name:
    #For loop will take each and every character of the string and print it with \n added in the last
    print(letter)
    print(letter.capitalize())
    print(letter.isalpha())

#for i in 100:#this will throw error, since number is not iterable
#    print(i)

#Immutable (not updatable)
#my_name[0]='M'#Doesn't work, because str is immutable

#Simple type
#Number Type: (int,float,complex number)
#String type: NOT an INDEXED SEQUENCED, NOT ITERABLE(LOOPING), Immutable(non updatable)
age=43
print(age)
print(type(age))
#print(age[0])#Will not work because non indexed or non sequenced
#age[1]=4 #immutable
age=age+1#possible due to reassigning of value to a variable is always possible
#Still immutable as per the below example
'''
>>> age=43
>>> bytes(age)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> memoryview(bytes(age))
<memory at 0x0000016C32183C40>
>>> age=age+1
>>> memoryview(bytes(age))
<memory at 0x0000016C32183D00>
'''

#float data type (alternative for float is decimal, double - these types are not directly available in python)
height=5.11 #Datatype is float - scale & precision for fraction numbers
print(height)
print(type(height))

#complex number type (not much important because in DE/AI world we don't use, it is used in electronics circuit design, mathematical expressions) - just know about it
circuit_frequency=5+4j#complex number with real + imaginary jewel part
print(circuit_frequency)
print(type(circuit_frequency))
print(circuit_frequency.real)
print(circuit_frequency.imag)

#Simple Type:
#Boolean Type : Very very important type used for making decisions.
# Logical output type produced when you perform comparison/binary or/and logical operations,
# which stores only 2 values (True or False)
a=10
b=20
print(a>b)#Comparison Return False
print(a<b)#Return True
print(type(a>b))#Print bool type

print(a>b or b>a)#Logical Return True
print(type(a>b or b>a))

#Sequence/Complex/Collection Type:
#To hold collection of values, not single value in a variable.
#First cut understanding of complex types in python (just for the better learning of looping constructs)
#4 collection types (set, tuples, dict, list), in an order of importance
#1. list
#2. dict
#3. tuple
#4. set

#All complex/collection types are ITERABLE
#1. list []- indexed sequenced collection of homogeneous(non mandatory) mutable items/elements.
#                   0       1       2           3       4
aspirants_list=['Uvaraj','Jamuna','Nathiya','Kalyani','Abi']
aspirants_list.append('Ashima')
print(aspirants_list)
print(aspirants_list[0])#use index to select an element/item
for i in aspirants_list:
    print(i)

#2. dict {key1:val1,key2:val2}- Non Indexed but Sequenced (because iterable) Collection of key & value pair.
#not possible        0               1       2           3           4
aspirants_dict={'Uvaraj':31,'Jamuna':30,'Nathiya':29,'Kalyani':23,'Abi':20}
print(aspirants_dict)
print(aspirants_dict['Uvaraj'])#use key to select a value (because it is not indexed)
for i in aspirants_dict.keys():
   print(i)
for i in aspirants_dict.values():
   print(i)
for i in aspirants_dict.items():
   print(i)

#3. Tuple () - Indexed Sequenced Collection of hetrogeneous (non mandatory) elements.
aspirant_tuple1=('Uvaraj',31,'Chennai','IT Professional')
aspirant_tuple2=('Jamuna',30,'Hyderabad','IT Professional')
for i in aspirant_tuple1:
    print(i)

#4. Set {} - Sequenced Collection of deduplicated homogeneous (non mandatory) items.
#It is majorly used for deduplicating & for set operations
set1={1, 20, 100, 4, 'x', 200, 10, 20}
print(set1)#deduplicated elements

set1={'Jamuna','Uvaraj','Sojiv'}
set2={'Tajamul','Uvaraj'}
print(set1)
print(set1)#deduplicated elements
print(set1.union(set2))#deduplicated union of both set elements
print(set1.difference(set2))#set1 minus set2 elements

#I have list of values list1=['Jamuna','Uvaraj','Sojiv','Jamuna','Uvaraj'],
#I want to remove duplicate items in it?
list1=['Jamuna','Uvaraj','Sojiv','Jamuna','Uvaraj']
set1:set=list1 #No, the "set" I have mentioned here is just a 'HINT', it will not have any impact on the type.
#To achieve the usecase, we have to convert the type by using conversion/casting functions
set1=set(list1)#converting to set to de duplicate
list1=list(set1)#Result has to be a set as per the requirement


#Misc types (None, range, bytes, memoryview)
#None is an no/unknown/null type in python
aspirants_count:int=None #Before 9AM, I am setting this aspirants count as none bcz i don't know how many will join today
#At 9AM
aspirants_count=55
#At 9.10AM
aspirants_count=75
#At 9.30AM
aspirants_count=99
#At 12.30PM
aspirants_count=86

x=print("a")#print return none after printing the content in the screen (output device)
print(x)

#range is a iterable type returned as an output of a range function that help us generate range of values
# with starting, until(end) and increments
rng:range=range(10)
print(rng)
print(list(rng))
print(type(rng))
print(list(range(0,11,2)))#This is a range of values starting with 0, until 11 (end at 10), increment of 2

#Bytes type is used to hold data in bytecode/encoded format
#Every data passed through network or memory or stored in disk are converted to objects for security, performance etc.,
age=43
byteformat=bytes(age)
print(byteformat)
memoryview1=memoryview(byteformat)
print(memoryview1)

name='Irfan'
byteformat=name.encode()
print(byteformat)
memoryview1=memoryview(byteformat)
print(memoryview1)

#Type conversion & Hinting
#Hinting of datatypes in python
#hint for human not for python
weight:float=None#Hint of 'float' is just for understanding the type for later reassignment,
# Based on dynamic inference this weight is defined as NoneType
print(type(weight))
weight=100.3#Based on dynamic inference this weight is inferred as float type, not based on the hint
print(type(weight))

#Type conversion
weight:float=100#Still int type, Based on the value the type is inferred dynamically (we can't change this character)
print(type(weight))
#We can cast or change it later by using type conversion functions
weight=float(weight)#Now it become float type
print(type(weight))

#Standard Input (input) & Output (print) & format ('f' string formatting) functions
#Standard input function
name=input("Enter your name:")#Get input from user at run time
print("name of the person is ",name)

age:int=int(input("Enter your age:"))#Converting the type after getting input from user
print(type(age))
#Check whether the given input is of type int or not?
print(isinstance(age,int))
print("age of the person is ",age)

#Standard Output function
name=input("Enter your name:")
print(name,end='~')#End is used to override the default new line in every value printed
print(name,age,sep=',')#sep is used to use seperator of any character other than default of space.

#String format function.















list_cols_tuple_records=[(1225655944140,'Business',36684.82,358),
(8876511923411,	'Business',	41813.13,	680),(6190138352945,'Savings',45432.27,466)]
























#select * from  odsdb_Rathan.ods_accounts where accountid=1225655944140;

for row in list_cols_tuple_records:#select * from  odsdb_Rathan.ods_accounts
    if row[0]==1225655944140:#where accountid=1225655944140
        print(row)






