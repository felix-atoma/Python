import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: NumPy array and mean
array = np.arange(1, 11)
mean_value = np.mean(array)
print("Mean of array 1 to 10:", mean_value)

# Task 2: Pandas DataFrame and summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Score': [88, 92, 85, 95, 90]
}
df = pd.DataFrame(data)
print("\nSummary Statistics:")
print(df.describe())

# Task 3: Fetch data from public API
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    bitcoin_price_usd = data['bpi']['USD']['rate']
    print("\nCurrent Bitcoin Price in USD:", bitcoin_price_usd)
except Exception as e:
    print("\nFailed to fetch Bitcoin data:", e)

# Task 4: Matplotlib line graph
numbers = [1, 3, 5, 7, 9]
plt.figure(figsize=(6, 4))
plt.plot(numbers, marker='o')
plt.title('Simple Line Graph')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.tight_layout()
plt.show()
