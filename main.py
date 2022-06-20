import database
import parser
import settings
from castomPrint import customPrint


def write_settings():
    settings.write_settings()



def main():
    """Конфигуратор"""
    customPrint.print_logo()
    current_vacancy = database.get_config('vacancy')
    if current_vacancy is None:
        print(f"Конфиг не настроен, перехожу к его настройке\n")
        write_settings()
    else:    
        print(f"Текущий конфиг:\n{current_vacancy}\n")
        config = input ("Настраиваем конфиг? (да/нет): ")
        if config.lower() == 'да':
            write_settings()
    parser.Parser()
    
 

    
if __name__ == '__main__':
    main()
 