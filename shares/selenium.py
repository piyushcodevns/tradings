from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle

options= Options()
driver=webdriver.Chrome(options=options)
driver.get("https://finance.yahoo.com/quote/MRF.NS/history/")
data=driver.page_source
datafile=open("mrf.txt","wb+")
pickle.dump(data,datafile)
datafile.flush()
datafile.close()
print(data)
driver.quit()