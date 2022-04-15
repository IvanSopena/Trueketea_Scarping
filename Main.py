# Script en python para la extraccion de los precios de los productos con el objetivo de
# crear un dataset.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import pymongo

class Extraccion_Precios:
    
    def __init__(self):
        self.MONGODB_HOST = "localhost"     #192.168.142.128
        self.MONGODB_PORT = '27017'
        self.MONGODB_TIMEOUT = 1000
        self.path = 'C:/chromedriver.exe'    
        self.URI_CONNECTION = "mongodb://" + self.MONGODB_HOST + ":" + self.MONGODB_PORT +  "/"

    def scraping(self):
        self.driver = webdriver.Chrome(self.path)
        self.driver.get ('https://es.wallapop.com/')
        button = self.driver.find_element_by_id('didomi-notice-agree-button')
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        self.driver.find_element_by_link_text("Motor y Accesorios").click()
        self.driver.implicitly_wait(10)
        button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div[1]/div/form/input')
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        button = self.driver.find_element_by_xpath('//*[@id="btn-load-more"]/button')
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        self.driver.implicitly_wait(10)
        button = self.driver.find_element_by_xpath('//*[@id="access-modal"]/div/div[2]/svg')
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        
        last_height = self.driver.execute_script('return document.body.scrollHeight')
        while True:
           self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
           time.sleep(2)
           new_height = self.driver.execute_script('return document.body.scrollHeight')
           
           if new_height == last_height:
               break
           last_height = new_height
        
    def connect(self):
        
       try:
           client = pymongo.MongoClient(self.URI_CONNECTION, serverSelectionTimeoutMS=self.MONGODB_TIMEOUT)
           client.server_info()
           print ('OK -- Connected to MongoDB at server %s' % (self.MONGODB_HOST))
           client.close()
       except pymongo.errors.ServerSelectionTimeoutError as error:
           print ('Error with MongoDB connection: %s' % error)
       except pymongo.errors.ConnectionFailure as error:
           print ('Could not connect to MongoDB: %s' % error)


    def inicio(self):  
       #self.connect()
       self.scraping()
    
if __name__ == "__main__":
    Extraccion_Precios().inicio()  
    