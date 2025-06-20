import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"API_SP.POP.TOTL_DS2_en_csv_v2_403333\API_SP.POP.TOTL_DS2_en_csv_v2_403333.csv",skiprows=4) #copy the path by rigth clicking the file and paste it 
print("Missing values:\n", df.isnull().sum())

df = df.drop(columns=["Indicator Name", "Indicator Code", "Country Code"])

df = df[["Country Name", "2022"]].dropna()

df.columns = ["Country", "Population_2022"]

print(df.head())

plt.figure(figsize=(10, 6))
plt.hist(df['Population_2022'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Total Population by Country (2022)')
plt.xlabel('Population (in millions)')
plt.ylabel('Number of Countries')
plt.grid(axis='y')
plt.show()

top10 = df.sort_values(by="Population_2022", ascending=False).head(10)


plt.figure(figsize=(12, 6))
plt.bar(top10["Country"], top10["Population_2022"] / 1e6, color='teal')
plt.title("Top 10 Most Populous Countries in 2022")
plt.xlabel("Country")
plt.ylabel("Population (in millions)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
