#MS/Ora/Google
#father->child = irfan@kader
class GenericUtils():#new1
    def cool_method(self,temp):#Member/Child
        try:
            print(f"class method - logic to set cool temp of {temp}")
            return str(temp) + 'is set on my AC'
        except Exception as ex_msg:
            print(f"cool temp failed due to : {ex_msg}, some other error")

    def clean_method(self):#new2
        try:
            print(self)
            print(f"class method - logics to clean AC")
            return 'AC is cleaned'
        except Exception as ex_msg:
            print(f"Cleaning failed due to : {ex_msg}, some other error")

class GoogleSearchEngine():#Class classname(class):
    def __init__(self,arg1,arg2,arg3):
        if arg1=='normal':
            print("User clicked normally, hence setting the window in this colors",arg2,arg3)
        else:
            print("User clicked incognito, hence setting the window in these plain colors", arg2, arg3)
    def search(self,searchstring):
        return "Output of Search "
    def genai(self,prompt):
        return "Output of generated content wrt the prompt "

tab1_regular=GoogleSearchEngine('normal','background-white','logo-colorful')
tab1_regular.search("when is diwali 2026?")
tab1_regular.genai("Who is Inceptez?")

tab2_icognito=GoogleSearchEngine('incognito','background-black','logo-grey')
tab2_icognito.search("when is diwali 2026?")
tab2_icognito.genai("Who is Inceptez?")