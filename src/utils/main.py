import os

def system(value:str) :
    return os.system(value)

def clear() :
    return os.system("clear")

    
def sleep(time:int):
    return os.system(f"sleep {time}")
