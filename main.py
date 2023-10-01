import matplotlib.pyplot as plt
import pandas as pd

# Import Data
data = pd.read_csv('data-1.csv',
                   parse_dates=['datetime']).dropna()
# DataFrame
df = pd.DataFrame(data)

# Add week days
df['day_of_week'] = df['datetime'].dt.day_name()

# Unique values in the 'parking' column and convert them to a list
parking = df['parking']
parking_list = parking.unique().tolist()

# Create Parkings List
parking_list = ['CLEMENCEAU', 'CONDORCET', 'DARCY', 'DAUPHINE', 'GRANGIER', 'MALRAUX', 'MONGE', 'SAINTE-ANNE', 'TIVOLI', 'TREMOUILLE']

# Calculate the average percentage for each day of the week for all parking locations
avg_percentage_by_day = df.groupby(['day_of_week', 'parking'])['pourcentage'].mean().unstack().round(2)

# Reorder the days of the week for proper sorting in the plot
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
avg_percentage_by_day = avg_percentage_by_day.reindex(week_days)

print(avg_percentage_by_day)

# Filter data for CLEMENCEAU and TREMOUILLE
clem = df[df['parking'] == 'CLEMENCEAU']
tremo = df[df['parking'] == 'TREMOUILLE']
monge = df[df['parking'] == 'MONGE']


# Visualise median percentage of parkings for each day
fig, ax = plt.subplots(figsize=(16, 6))  # Create a figure and axis

ax.plot(week_days, avg_percentage_by_day['CLEMENCEAU'], label='CLEMENCEAU')
ax.plot(week_days, avg_percentage_by_day['TREMOUILLE'], label='TREMOUILLE')
ax.plot(week_days, avg_percentage_by_day['MONGE'], label='MONGE')

ax.legend()
plt.show()


# Replace Negative Percentage
def replace_negatives(x):
    if x < 0:
        return 0
    else:
        return x

df['pourcentage'] = df['pourcentage'].apply(replace_negatives)

# Plotting
fig, ax = plt.subplots(figsize=(16, 6))  # Create a figure and axis

# Plot data for CLEMENCEAU
ax.plot(clem['datetime'], clem['pourcentage'], label='CLEMENCEAU')

# Plot data for TREMOUILLE
ax.plot(tremo['datetime'], tremo['pourcentage'], label='TREMOUILLE')

ax.set_title('Parking Percentage')
ax.set_xlabel('Date')
ax.set_ylabel('Percentage')
ax.legend()
plt.show()
