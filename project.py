import pandas as pd

df = pd.read_csv("sales.csv")
print(df)
df["Total_Sales"]=df["Price"]*df["Quantity"]
print(df)
print("Total Revenue:",df["Total_Sales"].sum())
top_products=df.groupby("Product")["Total_Sales"].sum()
print(top_products)
top_products=df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
print(top_products)
city_sales=df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False)
print(city_sales)
top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
print("Top Products:\n", top_products)
city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False)
print("\nCity Sales:\n", city_sales)
import matplotlib.pyplot as plt

top_products.plot(kind="bar")
plt.title("Top Products Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()
city_sales.plot(kind="bar")
plt.title("City Wise Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.show()