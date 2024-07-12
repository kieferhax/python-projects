import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'path_to_your_file/Summer-Olympic-medals-1976-to-2008.csv'
olympic_history_df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(olympic_history_df.head())

# Filter the data for host countries and relevant years
host_countries = {
    2004: 'Greece',
    2008: 'China',
    2012: 'United Kingdom',
    2016: 'Brazil',
    2020: 'Japan',
    2024: 'France'
}

# Initialize a dictionary to store medal counts for each host country
medal_counts = {year: {} for year in host_countries.keys()}

for year, country in host_countries.items():
    # Filter data for the host country in the hosting year
    host_data = olympic_history_df[(olympic_history_df['Year'] == year) & (olympic_history_df['Country'] == country)]
    medal_counts[year]['Gold'] = host_data['Gold'].sum()
    medal_counts[year]['Silver'] = host_data['Silver'].sum()
    medal_counts[year]['Bronze'] = host_data['Bronze'].sum()
    medal_counts[year]['Total'] = host_data[['Gold', 'Silver', 'Bronze']].sum().sum()

# Convert the medal_counts dictionary to a DataFrame
medal_counts_df = pd.DataFrame(medal_counts).T

# Plot the medal counts for host countries
medal_counts_df.plot(kind='bar', figsize=(10, 6))
plt.title('Medal Counts for Host Countries (2004-2024)')
plt.xlabel('Year')
plt.ylabel('Number of Medals')
plt.xticks(rotation=45)
plt.legend(title='Medal Type')
plt.show()

# Print the medal counts DataFrame
print(medal_counts_df)