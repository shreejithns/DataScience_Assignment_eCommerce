import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
customers = pd.read_csv('Customers.csv')
products = pd.read_csv('Products.csv')
transactions = pd.read_csv('Transactions.csv')

# Preview data
print(customers.head())
print(products.head())
print(transactions.head())

# Check for missing values
print(customers.isnull().sum())
print(products.isnull().sum())
print(transactions.isnull().sum())

# Analyze customers by region
region_counts = customers['Region'].value_counts()
print("Customers by region:\n", region_counts)

# Visualize customers by region
sns.countplot(y='Region', data=customers)
plt.title('Customers by Region')
plt.show()

# Monthly revenue analysis
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])
transactions['Month'] = transactions['TransactionDate'].dt.to_period('M')
monthly_revenue = transactions.groupby('Month')['TotalValue'].sum()
print("Monthly Revenue:\n", monthly_revenue)

# Plot monthly revenue
monthly_revenue.plot(kind='line', figsize=(10, 6), title='Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()
