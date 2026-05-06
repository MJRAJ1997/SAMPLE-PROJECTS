#sample project
import pandas as pd
import scipy
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('motorcyclessales.csv')
print(df.head())
df.info()
df.isnull()
df.describe()
plt.figure(figsize=(20,20))
plt.subplot(4,2,1)
plt.bar(df.CUSTOMERNAME,df.QUANTITYORDERED)
plt.xlabel("CUSTOMERNAME")
plt.ylabel("QUANTITYORDERED")
plt.title("quantity ordered based on customers")
plt.subplot(4,2,2)
plt.plot(df.COUNTRY,df.SALES,marker='o')
plt.xlabel("COUNTRY")
plt.ylabel("SALES")
plt.title("sales based on country ")
plt.legend(df.SALES)
#plt.figure(figsize=(20,20))
plt.subplot(4,2,3)
plt.pie(df.Profit,labels=["Madrid","NYC","Kobenhavn","Nantes","Manchester","Torino","Tsawassen","Bruxelles","Montreal"],autopct="%1.1f%%")
plt.xlabel("CITY")
plt.ylabel("Profit")
plt.title("profits based on city")
plt.tight_layout()
plt.show()
