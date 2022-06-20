from art import tprint


class customPrint(object):
    def __init__(self) -> None:
        pass

    def print_logo():    
        tprint("Head Hunter Bot")  

    def print_warn(text:str):
        print(f"<WARN> {text}\n")

    def print_error(text:str):
        print(f"<ERROR> {text}\n")  
        
    def print_info(text:str):
        print(f"<INFO> {text}\n")  

    def system_space():
        print(f'\n\n\n<SYSTEM LOG> Системный отступ\n')     
    

    