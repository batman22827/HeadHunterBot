import database




class write_settings(object):
    def __init__(self) -> None:
        self.get_vacancy()
        self.get_name_vacancy()
        self.get_name_company()
        self.get_description_vacancy()
        self.get_specialization_vacancy() 
        self.get_region()
        self.get_earnings()
        self.get_exp()
        self.get_employment()
        self.get_schedule()

    def get_vacancy(self):
        """Получение информации о требуемой вакансии"""
        res = input("Какую вакансию будем искать?: ").strip()
        database.write_config(row='vacancy',value=res)

    def get_name_vacancy(self):
        """Искать только в названии вакансии"""    
        res = input("Искать только в названии вакансии? (да/нет): ").strip()
        if res.lower() == 'да':
            database.write_config(row='only_name', value=True)  

        elif res.lower() == 'нет':
            database.write_config(row='only_name', value=False)  

    def get_name_company(self):
        """Искать только в названии компании"""    
        res = input("Искать только в названии компании? (да/нет): ").strip()
        if res.lower() == 'да':
            database.write_config(row='only_name_company',value=True) 

        elif res.lower() == 'нет':
            database.write_config(row='only_name_company',value=False)         

    def get_description_vacancy(self):
        """Искать только в описании вакансии"""    
        res = input("Искать только в описании вакансии? (да/нет): ").strip()

        if res.lower() == 'да':
            database.write_config(row='only_description',value=True) 

        elif res.lower() == 'нет':
            database.write_config(row='only_description',value=False)       

    def get_specialization_vacancy(self):
        res = input("По какой специализации ищем? (ПИСАТЬ СТРОГО С САЙТА либо оставьте строку пустой ) : ").strip()
        database.write_config(row='specialization',value=res)

    def get_industry(self):
        res = input("Какая отрасль компании ? (ПИСАТЬ СТРОГО С САЙТА либо оставьте строку пустой) : ").strip()
        database.write_config(row='industry',value=res)

    def get_region(self):
        res = input("В каком регионе ищем вакансии ? (либо оставьте строку пустой) : ").strip()
        database.write_config(row='region',value=res)

    def get_earnings(self):
        res = input("Какой уровень дохода ? (либо оставьте строку пустой) : ").strip()
        database.write_config(row='earnings',value=res)

    def get_exp(self):
        res = input("Укажите требуемый опыт работы (ПИСАТЬ СТРОГО С САЙТА либо оставьте строку пустой) : ").strip()
        database.write_config(row='exp',value=res)

    def get_schedule(self):
        res = input('График работы (ПИСАТЬ СТРОГО С САЙТА либо оставьте строку пустой) :  ').strip()
        database.write_config(row='schedule',value=res)                  

    def get_employment(self):
        res = input('Тип занятости (ПИСАТЬ СТРОГО С САЙТА либо оставьте строку пустой) :  ').strip()
        database.write_config(row='employment',value=res)   

