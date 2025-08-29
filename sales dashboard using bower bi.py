import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Define parameters
regions = ['North', 'South', 'East', 'West']
products = ['A', 'B', 'C', 'D']
months = pd.date_range(start='2024-01-01', periods=12, freq='ME')

# Generate synthetic data
data = []
for region in regions:
    for product in products:
        for month in months:
            revenue = np.random.randint(5000, 20000)
            growth = np.random.uniform(-0.1, 0.3)  # -10% to +30%
            data.append({
                'Region': region,
                'Product': product,
                'Month': month,
                'Revenue': revenue,
                'GrowthRate': round(growth, 2)
            })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV for Power BI
df.to_csv('synthetic_sales_data.csv', index=False)
print("Synthetic sales data saved as 'synthetic_sales_data.csv'")
