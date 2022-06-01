# Script en python para la extraccion de los precios de los productos con el objetivo de
# crear un dataset en la base de datos SQL SERVER.

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
import pyodbc

class Extraccion_Precios:

        self.path = '/Users/ivan/Downloads/chromedriver'    
        self.server = '192.168.1.51' 
        self.database = 'Trueketea' 
        self.username = 'tkadmin' 
        self.password = 'mypassword' 
        self.cursor

     def scraping(self):
         #Agregamnos la direccion web sobre la que se va a realizar la extracción
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



        #Realizamos un bucle que recorre las distintas secciones para extraer datos
        #Solamente se hace la estraccion de 3 secciones aunrque se pueden añadir mas
        for seccion in range(1,2):

            with switch(seccion) as s:
                
                if s.case(1, True):

                    #informática
                    seccion = self.driver.find_element_by_xpath('//*[@id="s-refinements"]/div/ul/li[9]/span/a')
                    ActionChains(self.driver).move_to_element(seccion).click(seccion).perform()
                    
                    self.extrac_info(4)

                if s.case(2, True):

                    #Bebés
                    seccion = self.driver.find_element_by_xpath('//*[@id="s-refinements"]/div/ul/li[20]/span/a')
                    ActionChains(self.driver).move_to_element(seccion).click(seccion).perform()
                    
                    self.extrac_info(9)

               

    def extrac_info(self,category)

         #Recorremos la lista hasta 20 elementos
         for objeto in range(2,20):

            #Hacemos la extraccion de los datos
            product-name = self.driver.find_element_by_xpath ('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div['+str(objeto)+']/div/div/div/div/div[3]/div[1]/h2/a/span').text
            price = self.driver.find_element_by_xpath ('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div['+str(objeto)+']/div/div/div/div/div[3]/div[3]/div/span[2]').text

            #Insertamos en la base de datos
            count = self.cursor.execute("""INSERT INTO Trueketea.ProductPrice ( Categorie_Id, ProductName, Price) VALUES ("'"+ category + "','"+  +"','"+  +"')""""",'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount
            cnxn.commit()

            if count == 0:
                print('Error al insertar ')



    def connect(self):

        #Función para realizar la conexión con la base de datos SQL SERVER
        try:
           cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
           self.cursor = cnxn.cursor()

       except pymongo.errors.ServerSelectionTimeoutError as error:
           print ('Error with SQL SERVER connection: %s' % error)
       except pymongo.errors.ConnectionFailure as error:
           print ('Could not connect to SQL SERVER: %s' % error)




	def inicio(self):  
       self.connect()
       self.scraping()
    
if __name__ == "__main__":
    Extraccion_Precios().inicio()  