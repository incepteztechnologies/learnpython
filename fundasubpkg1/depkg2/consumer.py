import learnpython.depkg2.fbp_module as fm
fm.cool_func(16)#module.fun(param)
fm.clean_func()


import learnpython.depkg2.oops_module as om
memobj1 = om.GenericUtils()#class is instantiated/constructed in memory in the form of Object - new3

memobj1.cool_method(17)#module.class.method(param) -> object.method()
memobj1.clean_method()

import learnpython.depkg2.oops_module as om#www.google.com
tab2=om.GenericUtils()#open a tab -> class is loaded in memory tab2
tab2.cool_method(17)#search engine method
tab2.clean_method()#genai method

#Constructors in Instantiating the Class
obj2=om.GenericUtils()#Construct class as an object with diff params passed