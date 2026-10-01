import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to your SQLite database
conn = sqlite3.connect('solaris_case_study.db')

# 2. Run the same aggregated query to get data for plotting
query = """
SELECT 
    category,
    ROUND(SUM(amt), 2) AS total_transaction_volume
FROM credit_data
WHERE amt >= 400 
   OR category IN ('travel', 'gas_transport', 'shopping_net', 'grocery_pos')
GROUP BY category
ORDER BY total_transaction_volume DESC;
"""

df_plot = pd.read_sql(query, conn)
conn.close()

# 3. Create a clean, professional bar chart using Matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df_plot['category'], df_plot['total_transaction_volume'], color='#2b5c8f', edgecolor='black', alpha=0.85)

# Add titles and labels
plt.title('Targeted Campaign Volume by Merchant Category (Solaris Case Study)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Merchant Category', fontsize=12, labelpad=10)
plt.ylabel('Total Transaction Volume ($)', fontsize=12, labelpad=10)
plt.xticks(rotation=30, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout so labels don't get cut off
plt.tight_layout()

# Save the chart as an image file that you can add to GitHub!
chart_filename = 'solaris_campaign_volume.png'
plt.savefig(chart_filename, dpi=300)
print(f"Success! Chart saved as '{chart_filename}'.")

# Display the chart on screen
plt.show()