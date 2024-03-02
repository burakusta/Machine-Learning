import pandas as pd
import numpy as np
filepath=r"C:\Users\burak\OneDrive\Masaüstü\auto.csv"
df = pd.read_csv(filepath, header=None)
headers = ["symboling","normalized-losses","make", "fuel-type","aspiration", "num-of-doors","body- style", "drive-wheels","engine-location","wheel-base", "length","width","height","curb- weight","engine-type", "num-of-cylinders", "engine-size","fuel- system","bore","stroke","compression-ratio","horsepower", "peak-rpm","city-mpg","highway- mpg","price"]
df.columns=headers
df1=df.replace('?',np.NaN)
#print(df1.head(1))
#df=df1.dropna(subset=["price"], axis=0)
#df.head(20)
#print(df[['length','compression-ratio']].describe())
#arr = np.array(df['length'])
print("df1 is \n",df1['normalized-losses'])
print(df['normalized-losses'])
df1[["normalized-losses"]] = df1[["normalized-losses"]].astype("float64")
#df_new=df1.dropna(subset=['normalized-losses'],axis=0)

#print("df dropped is \n",df_new['normalized-losses'])
#for_mean=(df1['normalized-losses'].mean(skipna=True))
#print(for_mean)
#my_ans=df_new["normalized-losses"].dtypes
my_ans=df1["normalized-losses"].dtypes

print(my_ans)
#df_new[["normalized-losses"]] = df_new[["normalized-losses"]].astype("float64")
#my_ans2=df_new["normalized-losses"].dtypes
#print(my_ans2)
for_mean=(df1['normalized-losses'].mean(skipna=True))
print(for_mean)
print(df1['normalized-losses'])
df1['normalized-losses']=df1['normalized-losses'].replace(np.NaN,for_mean)
print(df1['normalized-losses'])
max_value=df1['normalized-losses'].max()
min_value=df1['normalized-losses'].min()
#df_normalized1=df1
#df_normalized2=df1

#print("dfbins",df_bins['normalized-losses'])
df_normalized1=(df1['normalized-losses']-min_value)/(max_value-min_value)
print("normalizedddasasasa \n",df_normalized1)
print("değişti mi?",df1['normalized-losses'])


df_normalized2=(df1['normalized-losses']-df1['normalized-losses'].mean())-(df1['normalized-losses'].std())
print("noluyonormalizeddd \n",df_normalized2)
print(df1['normalized-losses'])

bins = np.linspace(min_value, max_value, 4)
print(bins)
group_names = ['Low', 'Medium', 'High']

df1['normalized-losses-binned'] = pd.cut(df1['normalized-losses'], bins, labels=group_names)
print(df1[['normalized-losses','normalized-losses-binned']] )
print(df1["fuel-type"])
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
print(dummy_variable_1)
#dummy_variable_1=dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'})
#print(dummy_variable_1)
#df1 = pd.concat([df1, dummy_variable_1], axis=1)
#print(df1)
#print("df changed is \n",replaced_df['normalized-losses'])
#print("mean= ",mean)
#print(df['length']+1)
#print(df1['normalized-losses'])
#print(df1['normalized-losses'].replace(np.NaN,mean))





