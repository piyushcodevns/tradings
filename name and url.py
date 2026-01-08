import pickle
name=input("Enter company name: ")
url=input("Enter company url: ")
try:
    with open("share.data","rb") as f:
        stocks=pickle.load(f)
except:
    stocks={}
stocks[name]=url
with open("share.data","wb") as f:
    pickle.dump(stocks,f)
print("Saved successfully")