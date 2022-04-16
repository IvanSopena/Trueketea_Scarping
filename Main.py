# Script en python para la extraccion de los precios de los productos con el objetivo de
# crear un dataset.

import json
import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
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
        self.path = '/Users/ivan/Downloads/chromedriver'    
        self.URI_CONNECTION = "mongodb://" + self.MONGODB_HOST + ":" + self.MONGODB_PORT +  "/"
        self.data = {}
        self.COLLECTION
       

    def scraping(self):
        #Agregamnos la direccion IP
        self.driver = webdriver.Chrome(self.path)
        self.driver.get ('https://www.amazon.es/b?node=3582001031')
        
        #Eliminamos el mensaje de aviso de cookies
        button = self.driver.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        
        #Seleccionamos en la lista desplegable la zona de busqueda
        selector = self.driver.find_element_by_xpath('//*[@id="searchDropdownBox"]')
        drop=Select(selector)
        drop.select_by_visible_text("Amazon Warehouse") 
        
        #Presionamos el boton de busqueda sin texto para ir a la pagina presencial
        searchBox = self.driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
        ActionChains(self.driver).move_to_element(searchBox).click(searchBox).perform()
        
        #Seleccionamos las secciones deonde vamos a sacar la informacion de los objetos
        
        for i in range(1,3):
            
           if i == 1:
               #informática
               seccion = self.driver.find_element_by_xpath('//*[@id="s-refinements"]/div/ul/li[9]/span/a')
               ActionChains(self.driver).move_to_element(seccion).click(seccion).perform()
               
               dir = "/Users/ivan/Downloads/"  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
               file_name = "data.json"
               
                             
               for objeto in range(2,20):
                   
                   if objeto != 5:
                       name_product = self.driver.find_element_by_xpath ('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div['+str(objeto)+']/div/div/div/div/div[3]/div[1]/h2/a/span').text
                       price = self.driver.find_element_by_xpath ('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div['+str(objeto)+']/div/div/div/div/div[3]/div[3]/div/span[2]').text
                       
                       self.data['Products_Price'].append({
                            'Categoria': '4',
                            'Precio': price,
                            'Producto': name_product})
                  
                   
               with open(file_name, 'w') as file:
                   json.dump(self.data, file)
              x = mycol.insert_one(mydict)
               

            if i == 2:
                #bebés
                seccion = self.driver.find_element_by_xpath('//*[@id="s-refinements"]/div/ul/li[20]/span/a')
                ActionChains(self.driver).move_to_element(seccion).click(seccion).perform()

                dir = "/Users/ivan/Downloads/"  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
                file_name = "data.json"
           
                for objeto in range(1,20):      
                    name_product = self.driver.find_element_by_xpath ('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div['+str(objeto)+']/div/div/div/div/div[3]/div[1]/h2/a/span').text
                       price = self.driver.find_element_by_xpath ('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div['+str(objeto)+']/div/div/div/div/div[3]/div[3]/div/span[2]').text
                       
                       self.data['Products_Price'].append({
                            'Categoria': '4',
                            'Precio': price,
                            'Producto': name_product})
           
            
            with open(file_name, 'w') as file:
                   json.dump(self.data, file)
              x = mycol.insert_one(mydict)
        

    def connect(self):
        
       try:
           client = pymongo.MongoClient(self.URI_CONNECTION, serverSelectionTimeoutMS=self.MONGODB_TIMEOUT)
           client.server_info()
           DB = client['Trueketea']
           self.COLLECTION = DB['Products_Price']
          
           print ('OK -- Connected to MongoDB at server %s' % (self.MONGODB_HOST))
           #client.close()
       except pymongo.errors.ServerSelectionTimeoutError as error:
           print ('Error with MongoDB connection: %s' % error)
       except pymongo.errors.ConnectionFailure as error:
           print ('Could not connect to MongoDB: %s' % error)


    def inicio(self):  
       #self.connect()
       self.data['Products_Price'] = []
       self.scraping()
    
if __name__ == "__main__":
    Extraccion_Precios().inicio()  
    