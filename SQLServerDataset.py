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

	def inicio(self):  
       #self.connect()
       self.data['Products_Price'] = []
       self.scraping()
    
if __name__ == "__main__":
    Extraccion_Precios().inicio()  