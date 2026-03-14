import pandas as pd

df = pd.read_excel("sales.xlsx")

print("=== SALES REPORT ===")

total = df["amount"].sum()
print("\nTotal Sales:" ,total)

customer = df.groupby("name")["amount"].sum()
top_customer = customer.sort_values(ascending=False).head(1)

name = top_customer.index[0]
amount = top_customer.values[0]

print("\nTop Customer:")
print(name, amount)

product = df.groupby("product")["amount"].sum().sort_values(ascending=False)
print("\nSales by Product")

for name, amount in product.items():
    print(name, ":", amount)
