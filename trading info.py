import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def get_live_price(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")
    trs = soup.find_all("tr")
    prices = []
    for tr in trs:
        tds = tr.find_all("td")
        try:
            price = tds[1].text.replace(",", "").strip()
            prices.append(float(price))
        except:
            pass
    return prices[-1]

username = input("Enter your name: ")
company = input("Enter company name: ")
quantity = int(input("Enter number of shares: "))


with open("share.data", "rb") as f:
    stocks = pickle.load(f)
url = stocks[company]
buy_price = get_live_price(url)
print("Live Buy Price:", buy_price)

trade = {
    "user": username,
    "company": company,
    "quantity": quantity,
    "buy_price": buy_price,
}

with open("trade.data", "wb") as f:
    pickle.dump(trade, f)

print(" SHARE BOUGHT SUCCESSFULLY")
