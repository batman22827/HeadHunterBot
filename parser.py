from re import I
import time
from urllib import response
import database
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from castomPrint import customPrint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from config import get_text_vacancy






class Parser(object):
    def __init__(self) -> None:
        self.resume = database.get_config('resume')
        self.text_vacancy = ""
        self.industry = database.get_config('industry')
        self.vacancy = database.get_config('vacancy')
        if self.resume !=None:
            self.text_vacancy = get_text_vacancy(f'{self.resume}')
        self.specialization = database.get_config('specialization')
        self.region = database.get_config('region')
        self.earnings = database.get_config('earnings')
        self.exp = database.get_config('exp')
        self.schedule = database.get_config('schedule')
        self.employment = database.get_config('employment')
        self.options = webdriver.ChromeOptions()


        self.options.add_argument('--no-sandbox')
        self.options.add_argument("--disable-notifications")
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('user-data-dir=C:/Users/Ilya/AppData/Local/Google/Chrome/User Data')
        self.options.add_argument("--log-level=3")
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4896.127 Safari/537.36")
        #self.options.add_argument('--headless')
        
        self.browser = webdriver.Chrome(executable_path='C:\\Programmist\\HeadHunter\\data\\chromedriver.exe',options=self.options)
        time.sleep(0.3)
        customPrint.system_space()
        self.check_response()
        
 
    def write_settings(self):
        self.browser.maximize_window()
        self.browser.get(url='https://hh.ru/search/vacancy/advanced')
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.CSS_SELECTOR,'#advancedsearchmainfield').send_keys(self.vacancy)
        self.click_search_only()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_specialization()
        self.click_industry()
        self.write_region()
        self.write_earnings()
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_experience()
        time.sleep(2)
        self.click_employment()
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.click_schedule()
        time.sleep(2)   
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.click_search_on_page()
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,'#submit-bottom').click() 
    
    
        self.click_vacancy()        
      
    def click_search_only(self):
        if database.get_config(config = 'only_name'):
            self.browser.find_element(By.XPATH,"//span[text()='в названии вакансии']").click()

        if database.get_config(config='only_name_company'):
            self.browser.find_element(By.XPATH,"//span[text()='в названии компании']").click()

        if database.get_config(config='only_description'):
            self.browser.find_element(By.XPATH,"//span[text()='в описании вакансии']").click()

    

    def click_specialization(self):
        self.browser.find_element(By.CSS_SELECTOR,"button[data-qa='resumesearch__profroles-switcher']").click()
        self.browser.find_element(By.CSS_SELECTOR,"body > div.bloko-modal-overlay.bloko-modal-overlay_visible > div > div.bloko-modal > div.bloko-modal-header > div > input").send_keys(self.specialization)
        if database.get_config(config='specialization'):    
            self.browser.find_element(By.XPATH,f"//span[text()='{self.specialization}']").click()
        self.browser.find_element(By.CSS_SELECTOR,"div.bloko-modal-footer > div > span:nth-child(2) > button").click()
    
    def click_industry(self):
            if database.get_config(config='industry'):   
                self.browser.find_element(By.CSS_SELECTOR,'#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-8.bloko-column_l-12.bloko-column_container > div > form > div:nth-child(5) > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-5.bloko-column_l-8 > div > div.form-choose > button').click()
                self.browser.find_element(By.CSS_SELECTOR,'body > div.bloko-modal-container.bloko-modal-container_visible > div.bloko-modal > div.bloko-modal-header > div.bloko-tree-selector-popup-search > input').send_keys(f'{self.industry}')    
                time.sleep(1)
                spans = self.browser.find_elements(By.CSS_SELECTOR,"span[class='bloko-checkbox__text']")
                for i in spans:
                    if i.text == self.industry: 
                        i.click()
                time.sleep(2)        
                self.browser.find_elements(By.CSS_SELECTOR,"[data-qa='bloko-tree-selector-popup-submit']")[1].click()
    
    def write_region(self):
        recorder_regions=self.browser.find_elements(By.CSS_SELECTOR,"span[class='bloko-tag-button                              Bloko-TagList-Remove']")
        time.sleep(2)
        for i in recorder_regions:
           i.click()
           time.sleep(0.5)
        self.browser.find_element(By.CSS_SELECTOR,"button[data-qa='resumes-search-region-selectFromList']").click()
        self.browser.find_element(By.CSS_SELECTOR,'.bloko-modal > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys(self.region)
        spans = self.browser.find_elements(By.CSS_SELECTOR,"span[class='bloko-checkbox__text']")
        for i in spans:
            try:
                if i.text == self.region: 
                    i.click()
            except:
                pass
                
            
        time.sleep(2)        
        self.browser.find_elements(By.CSS_SELECTOR,"[data-qa='bloko-tree-selector-popup-submit']")[1].click()


    def write_earnings(self):
        self.browser.find_element(By.CSS_SELECTOR,"input[data-qa='vacancysearch__compensation-input']").send_keys(f"{self.earnings}")

    def click_experience(self):
        if database.get_config(config='exp'):
            self.browser.find_element(By.XPATH,f"//span[text()='{self.exp}']").click()
    
    def click_employment(self):
        if database.get_config(config='employment'):
            self.employment = self.employment.split(',')
            for e in self.employment:
                self.browser.find_element(By.XPATH,f"//span[text()='{e}']").click()
                

    def click_schedule(self):
          if database.get_config(config='schedule'):
            self.schedule = self.schedule.split(',')
            for s in self.schedule:
                self.browser.find_element(By.XPATH,f"//span[text()='{s}']").click()#Расписание работы
    
    def click_search_on_page(self):
        self.browser.find_element(By.XPATH,f"//span[text()='100 вакансий']").click()

    def click_resume(self):
        pass

    def click_vacancy(self):
        customPrint.print_info(text='Начинаю поиск кнопок откликнуться')
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        vacancy= self.browser.find_elements(By.LINK_TEXT,"Откликнуться")
       
        customPrint.print_info(text='Все кнопки найдены')
        time.sleep(3)
        for i in vacancy:
            src = i.get_attribute('href')
            self.browser.execute_script(f"$(window.open('{src}'))")
            self.browser.switch_to.window(self.browser.window_handles[-1])
            check = self.checking_exsist('#RESPONSE_MODAL_FORM_ID > div.bloko-form-group > p')
            if check == True:
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[-1])
            elif check == False:    
                print(self.browser.current_url)
                time.sleep(2)
                try:
                    self.browser.find_element(By.CSS_SELECTOR,"#RESPONSE_MODAL_FORM_ID > div > div.bloko-form-row > button").click()
                except:
                    pass
                self.browser.find_element(By.XPATH,f"//span[text()='{self.resume}']").click()   
                self.browser.find_element(By.CSS_SELECTOR,'#RESPONSE_MODAL_FORM_ID > div > div.bloko-form-row > textarea').clear()
                self.browser.find_element(By.CSS_SELECTOR,'#RESPONSE_MODAL_FORM_ID > div > div.bloko-form-row > textarea').send_keys(f'{self.text_vacancy}')
                time.sleep(4)
                database.write_url(self.browser.current_url,False)
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[-1])
        customPrint.print_info("По всем найденным вакансия отклики отправлены!Завершаю работу")         

    def checking_exsist(self,selector):
        try:
            self.browser.find_element(By.CSS_SELECTOR,selector)
        except NoSuchElementException:
            return False
        return True
   
    def check_response(self):
        self.browser.maximize_window()
        self.browser.get(url='https://hh.ru/search/vacancy/advanced')
        self.browser.implicitly_wait(10)
        for i in database.get_all_urls():
            time.sleep(1)
            self.browser.execute_script(f"$(window.open('{i[0]}'))")
            self.browser.switch_to.window(self.browser.window_handles[-1])
            time.sleep(2)
            self.browser.find_element(By.CSS_SELECTOR,"#RESPONSE_MODAL_FORM_ID > div > div.vacancy-response > a").click()
            try:
                text_response = self.browser.find_element(By.CSS_SELECTOR,"div[class='bloko-text bloko-text_small'").text
                if text_response == 'Отказ' or text_response == 'Резюме просмотрено' or text_response == 'Приглашение':
                    try:
                        self.browser.find_element(By.CSS_SELECTOR,"#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div.g-col1.m-colspan3 > div > div.negotiations > div.negotiations-body > div:nth-child(2) > div.negotiations-message-body > form > div.negotiations-new-message.HH-Form-Element-TooltipElement > textarea").send_keys("123")
                    except:
                        print("Закрыты сообщения")
            except:
                print("Вакансия еще не просмотрена")            
        time.sleep(5455)    