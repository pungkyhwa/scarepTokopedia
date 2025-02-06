import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd


tokped_link = "https://www.tokopedia.com/search?st=&q=bimoli&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
driver = webdriver.Chrome()

try:
    driver.get(tokped_link)    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    rentang = 700
    for i in range(1, 10):
        akhir = rentang * i
        perintah = f"window.scrollTo(0, {akhir})"
        driver.execute_script(perintah)
        time.sleep(1)  

    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    list_nama,list_harga=[],[]
    for area in soup.find_all('div',class_='css-5wh65g'):
        nama = area.find('div',class_='_6+OpBPVGAgqnmycna+bWIw==').get_text()
        print(nama)
        list_nama.append(nama)

    
    for outer_div in soup.find_all('div', class_='XvaCkHiisn2EZFq0THwVug=='):
        price_div = soup.find('div', class_="_67d6E1xDKIzw+i2D2L0tjw==").get_text()
        # price = price_div.get_text()
        print(price_div)
        list_harga.append(price_div)

        # list_harga.append(price_div)
        print('--------------')
        
        

    # df = pd.DataFramedf = pd.DataFrame({'Nama':list_nama,'Harga':list_harga})

    # writer = pd.ExcelWriter('diapers.xlsx')
    # df.to_excel(writer,'Sheet1',index=False)
    # writer.save()


    
    df = pd.DataFrame({'Nama':list_nama,'Harga':list_harga})
    df.to_excel('tokped.xlsx', index=False, sheet_name='Sheet1')



finally:
    driver.quit()


