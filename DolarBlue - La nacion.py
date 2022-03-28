# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 23:09:17 2022

@author: Fede
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

html_text = requests.get("https://www.lanacion.com.ar/").text
soup = BeautifulSoup(html_text, "lxml")
dolar = soup.find("body", class_="ln")
dolar_c = dolar.find("span", id ="precioCompraBlue")
dolar_v = dolar.find("span", id ="precioVentaBlue")

dolar_c = dolar_c.string
dolar_v = dolar_v.string

while True:
    print("Dolar blue: " + dolar_c + " / " + dolar_v)
    print("\n")
    time.sleep(1)
















#JSON
[
     {"Doar blue" : 5
      
        
      }
 
 ]
