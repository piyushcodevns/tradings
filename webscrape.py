import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open("stock.data", "rb") as f:
    stocks = pickle.load(f)
    stockname = input("Enter the company name: ")
    url = stocks[stockname]
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    data = driver.page_source
    datafile = open("company.txt", "wb+")
    pickle.dump(data, datafile)
    datafile.flush()
    datafile.close()
    print(data)
    driver.quit()
