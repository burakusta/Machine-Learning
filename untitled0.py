import pandas as pd
#import csv
url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url, header=None)
print(df.head(3))
headers = ["symboling","normalized-losses","make", "fuel-type","aspiration", "num-of-doors","body- style", "drive-wheels","engine-location","wheel-base", "length","width","height","curb- weight","engine-type", "num-of-cylinders", "engine-size","fuel- system","bore","stroke","compression-ratio","horsepower", "peak-rpm","city-mpg","highway- mpg","price"]
df.columns=headers
print(df.tail(1))
path=r"C:\Users\burak\OneDrive\Masaüstü\cars.csv"
df1=pd.read_csv(path, header=None)
#df1.columns=headers
print("buradayımmmm\n",df1.head(1))
#df.to_csv(path) #??????????????
#print("buradayım???\n",print(df.index))
#print(df.index[2])
print(df.dtypes)
print(df.describe())
print(df.describe(include="all"))
print(df.info())
filepath=r"C:\Users\burak\OneDrive\Masaüstü\auto.csv"
df = pd.read_csv(filepath, header=None)
print("The last 10 rows of the dataframe\n") 
print(df.tail(10))
filepath=r"C:\Users\burak\OneDrive\Masaüstü\auto.csv"
df = pd.read_csv(filepath, header=None)
df.columns = headers
print(df.columns)