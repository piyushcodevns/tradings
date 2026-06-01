from bs4 import BeautifulSoup
import pickle

file = open("ril.txt", "rb")
data = pickle.load(file)
file.close()

soup = BeautifulSoup(data, "html.parser")

data_date = input("Enter date: ")
found = False
trs = soup.find_all("tr")
for tr in trs:
    tds = tr.find_all("td")
    if len(tds) == 7:
        row = []
        for td in tds:
            row.append(td.text.strip())
        if row[0] == data_date:
            found = True
            print("\nDATA FOUND")
            print("DATE:", row[0])
            print("OPEN:", row[1])
            print("HIGH:", row[2])
            print("LOW:", row[3])
            print("CLOSE:", row[4])
            print("ADJ CLOSE:", row[5])
            print("VOLUME:", row[6])
            break
if not found:
    print("\nINVALID DATE")
