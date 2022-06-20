import time

from matplotlib.font_manager import json_dump
import database
from distutils.command.check import check
from lib2to3.pgen2 import driver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from castomPrint import customPrint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from config import get_text_vacancy,write_data_qa_industry






class Parser(object):
    def __init__(self) -> None:
        self.vacancy = database.get_config('vacancy')
        self.text_vacancy = get_text_vacancy('бариста')
        self.specialization = database.get_config('specialization')
        self.region = database.get_config('region')
        self.earnings = database.get_config('earnings')
        self.exp = database.get_config('exp')
        self.schedule = database.get_config('schedule')
        self.employment = database.get_config('employment')
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument("--disable-notifications")
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("user-data-dir=C:\\Users\\Ilya\\AppData\\Local\\Google\\Chrome\\User Data")
        self.options.add_argument("--log-level=3")
        self.options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2171.95 Safari/537.36")
        self.browser = webdriver.Chrome(executable_path='C:\\Programmist\\AvtoBot\\data\\chromedriver.exe',options=self.options)
        time.sleep(0.3)
        customPrint.system_space()
        #self.write_settings()
        self.get_span_data_qa()
        
      
    def get_span_data_qa(self):
        self.browser.get(url='https://hh.ru')
        self.browser.find_element(By.CSS_SELECTOR,'.bloko-icon-dynamic').click()
        self.browser.find_element(By.CSS_SELECTOR,'#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-8.bloko-column_l-12.bloko-column_container > div > form > div:nth-child(5) > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-5.bloko-column_l-8 > div > div.form-choose > button').click()
        time.sleep(2)
        spans = self.browser.find_elements(By.CLASS_NAME,'bloko-checkbox__text')
        write_data_qa_industry(spans)

  
    def write_settings(self):
        self.browser.get(url='https://hh.ru')
       
        self.browser.find_element(By.CSS_SELECTOR,'.bloko-icon-dynamic').click()
       
        self.browser.find_element(By.CSS_SELECTOR,'#advancedsearchmainfield').send_keys(self.vacancy)
        if database.get_config(config = 'only_name'):
            self.browser.find_element(By.XPATH,"//span[text()='в названии вакансии']").click()

        if database.get_config(config='only_name_company'):
            self.browser.find_element(By.XPATH,"//span[text()='в названии компании']").click()

        if database.get_config(config='only_description'):
            self.browser.find_element(By.XPATH,"//span[text()='в описании вакансии']").click()
       
        self.browser.find_element(By.CSS_SELECTOR,"button[data-qa='resumesearch__profroles-switcher']").click()
       
        self.browser.find_element(By.CSS_SELECTOR,"body > div.bloko-modal-overlay.bloko-modal-overlay_visible > div > div.bloko-modal > div.bloko-modal-header > div > input").send_keys(self.specialization)
        self.browser.find_element(By.XPATH,f"//span[text()='{self.specialization}']").click()
        self.browser.find_element(By.CSS_SELECTOR,"div.bloko-modal-footer > div > span:nth-child(2) > button").click()

        self.browser.find_element(By.CSS_SELECTOR,'#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-8.bloko-column_l-12.bloko-column_container > div > form > div:nth-child(6) > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-5.bloko-column_l-8 > div > div > div > div.region-select.region-select_list > div > input').send_keys(self.region)
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,'#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-8.bloko-column_l-12.bloko-column_container > div > form > div:nth-child(8) > div > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-5.bloko-column_l-8 > div:nth-child(1) > div:nth-child(2) > input.bloko-input.bloko-input_sized.Bloko-FormattedNumericInput-Visible').send_keys(self.earnings)
        
        time.sleep(4)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        exp_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,f"//span[text()='{self.exp}']")))
        exp_button.click()
        
       
        self.employment = self.employment.split(',')
        for e in self.employment:
            employment_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,f"//span[text()='{e}']")))
            employment_button.click()
            self.browser.implicitly_wait(1)
        
        self.schedule = self.schedule.split(',')
        for s in self.schedule:
            self.browser.find_element(By.XPATH,f"//span[text()='{s}']").click()#Расписание работы
           
       
        self.browser.find_element(By.CSS_SELECTOR,'#submit-bottom').click() 
    
    
        self.click_vacancy()    

    def click_vacancy(self):
        customPrint.print_info(text='Начинаю поиск кнопок откликнуться')
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        vacancy= self.browser.find_elements_by_link_text("Откликнуться")
       
        customPrint.print_info(text='Все кнопки найдены')
        time.sleep(3)
        for i in vacancy:
            src = i.get_attribute('href')
            self.browser.execute_script(f"$(window.open('{src}'))")
            self.browser.switch_to.window(self.browser.window_handles[-1])
            check = self.checking_exsist('#RESPONSE_MODAL_FORM_ID > div.bloko-form-group > p')
            if check == True:
                print("Тест найден")
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[-1])
            elif check == False:    
                print("Нет теста")
                time.sleep(2)
                try:
                     self.browser.find_element(By.CSS_SELECTOR,'#RESPONSE_MODAL_FORM_ID > div > div.bloko-form-row > button').click()
                except:
                    pass    
                self.browser.find_element(By.CSS_SELECTOR,'#RESPONSE_MODAL_FORM_ID > div > div.bloko-form-row > textarea').clear()
                self.browser.find_element(By.CSS_SELECTOR,'#RESPONSE_MODAL_FORM_ID > div > div.bloko-form-row > textarea').send_keys(f'{self.text_vacancy}')
                time.sleep(4)
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[-1])
                
           
    def checking_exsist(self,selector):
        try:
            self.browser.find_element(By.CSS_SELECTOR,selector)
        except NoSuchElementException:
            return False
        return True
   