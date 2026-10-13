aspirants_cnt=100

def list_of_files(dir:str):
    import os
    list_of_files=os.listdir(dir)
    return list_of_files

def make_dir(dir:str):
    import os
    os.makedirs(dir,exist_ok=True)

