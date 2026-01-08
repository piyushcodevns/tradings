import pickle
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

file=open("company.txt","rb+")
data=pickle.load(file)
file.close()
soup=BeautifulSoup(data,"html.parser")
trs=soup.find_all("tr")
y=[]
for tr in trs:
    tds=tr.find_all("td")
    try:
        price=tds[1].text.replace(",","").strip()
        y.append(float(print))
    except:
        pass
    
x=list(range(len(y)))
x.reverse()

avgy=sum(y)/len(y)
starty=[y[-1] for i in range (len(y))]

if y[-1]>y[0]:
    color="red"
elif y[-1]<y[0]:
    color="red"
else:
    color="yellow"
    
plt.plot(x,y,color=color)
