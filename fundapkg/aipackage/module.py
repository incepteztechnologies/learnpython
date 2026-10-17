#FBP - DE/AI/BI
def a():
    pass

#OOPS + FBP
class Cls1():
    def a(self):#method
        print(self)#self holds the object of the class

#DE/AI/BI
obj1 = Cls1() #non param constructing the class in memory by using () hence object can be created
obj1.a()#
obj2 = Cls1()#One more object creation is meaning less, unnecessary memory occupation.
obj1.a()#

class Xls():#template/blueprint created commonly for multiple usage

    def tab1(self):
        return 'tab1 returning'
    def tab2(self):
        return 'tab2 returning'

screen_object1=Xls()#double click (), xls loaded in memory(RAM) , referring using the taskbar in the screen


class XlsParam:
    def __init__(self,color,no_of_cols=3):#special method called init we can enable parameterized constructor
        self.init_attribute=10#attribute of the class by using the initial self.variable name
        self.member_color=color#attribute is a member of this class
        self.member_no_of_columns=no_of_cols

    def tab1(self):#adding initial to method
        return f'{self.init_attribute} tab1 returning with {self.member_color} and no of cols {self.member_no_of_columns}'
    def tab2(self):#member method because self is pass as argument
        return f'tab2 returning with {self.member_color}'

aishwarya_object1 = XlsParam(color='yellow')#parameterized constructor
print(aishwarya_object1.tab1())
karthikeyan_object1 = XlsParam(color='blue')
print(karthikeyan_object1.tab1())
surendar_object1 = XlsParam('orange',4)
print(surendar_object1.tab1())


#from google import genai
class Client:
    def __init__(self,api_key='env_value'):
        self.api_key=api_key
    def ai_response(self,prompt):
        return f"result of the prompt by accessing google ai model using api key provided {self.api_key}"

#import module
client = Client(api_key="YOUR_GEMINI_API_KEY")