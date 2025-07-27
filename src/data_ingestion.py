import pandas as pd
import ssl
import certifi
import urllib.request
import os

url = "https://raw.githubusercontent.com/araJ2/customer-database/master/Ecommerce%20Customers.csv"

# ✅ Create a secure SSL context using certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())

# ✅ Read the CSV via urllib with proper SSL verification
with urllib.request.urlopen(url, context=ssl_context) as response:
    df = pd.read_csv(response)

# ✅ Same processing as before
df = df.iloc[:, 3:]
df = df[df["Length of Membership"] > 1]

df.drop(columns=["Avg. Session Length"], inplace=True)  # ✅ RIGHT


# ✅ Ensure the data folder exists
os.makedirs("data", exist_ok=True)

df.to_csv("data/customer.csv", index=False)
print("✅ Data saved to data/customer.csv")