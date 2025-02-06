import time
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

tokped_link = "https://www.tokopedia.com/search?st=product&q=laptop%20gaming&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="

driver = webdriver.Chrome()
driver.get(tokped_link)

rentang = 700
for i in range(1,10):
    akhir = rentang * i 
    perintah = "window.scrollTo(0,"+str(akhir)+")"
    driver.execute_script(perintah)
    
time.sleep(5)
list_nama,list_harga,list_terjual,list_link=[],[],[],[]
soup =  BeautifulSoup(driver.page_source,"html.parser")
for area in soup.find_all('div',class_='css-974ipl'):
    nama = area.find('div',class_='css-3um8ox').get_text()
    harga = area.find('div',class_='css-1ksb19c').get_text()
    terjual = area.find('span',class_='css-1duhs3e').get_text()
    link = area.find('a')['href']

    print (nama) 
    print (harga)
    print (terjual)
    print (link)
    print ('---------------------')


    list_nama.append(nama)
    list_harga.append(harga)
    list_terjual.append(terjual)
    list_link.append(link)

    df = pd.DataFramedf = pd.DataFrame({'Nama':list_nama,'Harga':list_harga,'Terjual':list_terjual,'Link':list_link})
    writer = pd.ExcelWriter('hasil.xlsx')
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()