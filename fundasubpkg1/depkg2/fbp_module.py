x:int=10

lst:list=list((10,20))
lst.append(30)

def cool_func(temp):
    try:
        print(f"logic to set cool temp of {temp}")
        return str(temp) + 'is set on my AC'
    except Exception as ex_msg:
        print(f"cool temp failed due to : {ex_msg}, some other error")

def clean_func():
    try:
        print(f"logics to clean AC")
        return 'AC is cleaned'
    except Exception as ex_msg:
        print(f"Cleaning failed due to : {ex_msg}, some other error")