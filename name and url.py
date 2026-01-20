import pickle
name = input("Enter company name: ")
url = input("Enter company url: ")
try:
    with open("stock.data", "rb") as f:
        stocks = pickle.load(f)
except:
    stocks = {}
stocks[name] = url
with open("stock.data", "wb") as f:
    pickle.dump(stocks, f)
print("Saved successfully")
