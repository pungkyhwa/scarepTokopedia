import time
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

tokped_link = "https://www.tokopedia.com/search?st=&q=bimoli&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
driver = webdriver.Chrome()
driver.get(tokped_link)
# driver = webdriver.Chrome()
# driver.get(tokped_link)

rentang = 700
for i in range(1,10):
    akhir = rentang * i 
    perintah = "window.scrollTo(0,"+str(akhir)+")"
    driver.execute_script(perintah)
    # print("loading ke-"+str(i))
    time.sleep(1)

soup =  BeautifulSoup(driver.page_source,"html.parser")

list_nama,list_harga = [],[]
for area in soup.find_all('div',class_='css-5wh65g'):
    nama = area.find('div',class_='VKNwBTYQmj8+cxNrCQBD6g==').get_text()
    print(nama)
    harga = area.find('div',class_='_8cR53N0JqdRc+mQCckhS0g==').get_text()
    print(harga)
    print("-------------")
    list_nama.append(nama)
    list_harga.append(harga)

df = pd.DataFramedf = pd.DataFrame({'Nama':list_nama,'Harga':list_harga})
writer = pd.ExcelWriter('diapers.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()