python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the SAIDI dataset
file_path = "SAIDI.csv"
data = pd.read_csv(file_path)

# Convert Year column to datetime
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Plot the SAIDI trend
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='SAIDI', data=data, marker='o', label='SAIDI')
plt.title('SAIDI Trends Over Time', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('SAIDI (Minutes per Customer)', fontsize=14)
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig("saidi_trend.png")
plt.show()

# Example of exporting the data to JSON format
data.to_json("SAIDI.json", orient='records', lines=True)
