from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Test_locators import locators
from Test_data import data


class Prem:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(data.Prem_Data().url)
    
    def invalid_login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Prem_locators().username_inputbox).send_keys(data.Prem_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Prem_locators().password_inputbox).send_keys(data.Prem_Data().invalid_passord)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().loginbutton).click()


    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Prem_locators().username_inputbox).send_keys(data.Prem_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Prem_locators().password_inputbox).send_keys(data.Prem_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().loginbutton).click()

    def add_employee(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().Pimbutton_locator).click()
        sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Prem_locators().Add_employee).click()
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Prem_locators().First_name).send_keys(data.Prem_Data().First_name)
        self.driver.find_element(by=By.NAME, value=locators.Prem_locators().Middle_name).send_keys(data.Prem_Data().Middle_name)
        self.driver.find_element(by=By.NAME, value=locators.Prem_locators().Last_name).send_keys(data.Prem_Data().Last_name)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators.Click_save).click()

    def Edit_employee(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().Pimbutton_locator).click()
        sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Prem_locators().Click_Employee_list).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().Edit_employee_details).click()
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Prem_locators().Edit_fristname).send_keys(data.Prem_Data().Edit_frist_name)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().Edit_click_save_button).click()
        

    def delete_employee(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().Pimbutton_locator).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().Delete_employee).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Prem_locators().Delete_yes).click()
        while(True):
            pass
          
      
Prem().invalid_login()
Prem().login()
Prem().add_employee()
Prem().Edit_employee()
Prem().delete_employee()