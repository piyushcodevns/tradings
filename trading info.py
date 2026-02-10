import pickle
from bs4 import BeautifulSoup


def get_live_price():
    with open("company.txt", "rb") as file:
        data = pickle.load(file)
    soup = BeautifulSoup(data, "html.parser")
    trs = soup.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) >= 2:
            try:
                price = tds[1].text.replace(",", "").strip()
                return float(price)
            except:
                pass
    return None


username = input("Enter your name: ")
company = input("Enter company name: ")
quantity = int(input("Enter number of shares: "))
with open("stock.data", "rb") as f:
    stocks = pickle.load(f)
if company not in stocks:
    print("Company not found ")
    exit()
buy_price = get_live_price()
print("Per share price:", buy_price)
total_cost = buy_price * quantity
print("Total cost of shares:", total_cost)
trade = {
    "user": username,
    "company": company,
    "per share price": buy_price,
    "quantity": quantity,
    "buy_price": buy_price,
}
with open("trade.data", "wb") as f:
    pickle.dump(trade, f)
print("SHARE BOUGHT SUCCESSFULLY")
