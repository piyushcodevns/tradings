import pickle
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# DATA LOAD

file = open("company.txt", "rb+")
data = pickle.load(file)
file.close()
soup = BeautifulSoup(data, "html.parser")
trs = soup.find_all("tr")
y = []
for tr in trs:
    tds = tr.find_all("td")
    try:
        price = tds[1].text.replace(",", "").strip()
        y.append(float(price))
    except:
        pass
    
# X AXIS

x = list(range(len(y)))
x.reverse()

# AVERAGE LINE 
  
avgy = sum(y) / len(y)
starty = [y[-1] for i in range(len(y))]

# COLOR LOGIC

if y[-1] > y[0]:
    color = "red"
elif y[-1] < y[0]:
    color = "green"
else:
    color = "yellow"
    
# PLOT

plt.plot(x, y, color=color)
plt.plot(x, starty, color="blue",linestyle="-.")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Stock Prices Over Time")
plt.show()
