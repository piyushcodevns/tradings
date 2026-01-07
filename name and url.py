import pickle
name = input("Enter stock name: ")
url = input("Enter stock url: ")
try:
    with open("share.dat", "rb") as f:
        stock = pickle.load(f)
except:
    stock = {}
stock[name] = url
with open("share.dat", "wb") as f:
    pickle.dump(stock, f)
print("Saved successfully")
