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
        self.MONGODB_HOST = "192.168.142.128"
        self.MONGODB_PORT = '27017'
        self.MONGODB_TIMEOUT = 1000
        self.driver = webdriver.Chrome('C://chromedriver.exe')    
        self.URI_CONNECTION = "mongodb://" + self.MONGODB_HOST + ":" + self.MONGODB_PORT +  "/"


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
       self.connect()  
    
if __name__ == "__main__":
    Extraccion_Precios().inicio()  
    