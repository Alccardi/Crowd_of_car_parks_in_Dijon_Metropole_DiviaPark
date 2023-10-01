import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Import Data
data = pd.read_csv('data-1.csv',
                   parse_dates=['datetime']).dropna()
# DataFrame
df = pd.DataFrame(data)

# Add week / days / months
df['day_of_week'] = df['datetime'].dt.day_name()
df['month'] = df['datetime'].dt.month_name()
df['week_number'] = df['datetime'].dt.isocalendar().week

print(df)

# Unique values in the 'parking' column and convert them to a list
parking = df['parking']
parking_list = parking.unique().tolist()

# Create Parkings List
parking_list = ['CLEMENCEAU', 'CONDORCET', 'DARCY', 'DAUPHINE', 'GRANGIER', 'MALRAUX', 'MONGE', 'SAINTE-ANNE', 'TIVOLI', 'TREMOUILLE']

# Calculate the average percentage for each day / month / week of the week for all parking locations
avg_percentage_by_day = df.groupby(['day_of_week', 'parking'])['pourcentage'].mean().unstack().round(2)
avg_percentage_by_month = df.groupby(['month', 'parking'])['pourcentage'].mean().unstack().round(2)
avg_percentage_by_week = df.groupby(['week_number', 'parking'])['pourcentage'].mean().unstack().round(2)

# Reorder the days of the week and months for proper sorting in the plot
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_numbers = list(range(1, 53))

avg_percentage_by_month = avg_percentage_by_month.reindex(months)
avg_percentage_by_day = avg_percentage_by_day.reindex(week_days)
avg_percentage_by_week = avg_percentage_by_week.reindex(week_numbers)

# Filter data for CLEMENCEAU and TREMOUILLE
clem = df[df['parking'] == 'CLEMENCEAU']
tremo = df[df['parking'] == 'TREMOUILLE']
monge = df[df['parking'] == 'MONGE']

# Function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center', color='darkblue')

# Visualise median percentage of parkings for weeks
fig, ax = plt.subplots(figsize=(16, 6))  # Create a figure and axis

# Plots by Day
ax.plot(week_days, avg_percentage_by_day['CLEMENCEAU'], label='CLEMENCEAU')
ax.plot(week_days, avg_percentage_by_day['TREMOUILLE'], label='TREMOUILLE')
ax.plot(week_days, avg_percentage_by_day['MONGE'], label='MONGE')

# Add Value Labels
addlabels(week_days, avg_percentage_by_day['CLEMENCEAU'])
addlabels(week_days, avg_percentage_by_day['TREMOUILLE'])
addlabels(week_days, avg_percentage_by_day['MONGE'])

# Title and Labels
ax.set_title('Parking Percentage by week')
ax.set_xlabel('Months')
ax.set_ylabel('Percentage')

# Add Legend
ax.legend()

# Add grid
plt.grid()

# Visualise median percentage of parkings for each day
fig, ax = plt.subplots(figsize=(16, 6))  # Create a figure and axis

# Plots by Week
ax.plot(week_numbers, avg_percentage_by_week['CLEMENCEAU'], label='CLEMENCEAU')
ax.plot(week_numbers, avg_percentage_by_week['TREMOUILLE'], label='TREMOUILLE')
ax.plot(week_numbers, avg_percentage_by_week['MONGE'], label='MONGE')

# Add Value Labels
addlabels(week_numbers, avg_percentage_by_week['CLEMENCEAU'].values)
addlabels(week_numbers, avg_percentage_by_week['TREMOUILLE'].values)
addlabels(week_numbers, avg_percentage_by_week['MONGE'].values)

# Title and Labels
ax.set_title('Parking Percentage by week')
ax.set_xlabel('Months')
ax.set_ylabel('Percentage')

# Add Legend
ax.legend()

# Add grid
plt.grid()


# Visualise median percentage of parkings for each month
fig, ax = plt.subplots(figsize=(16, 6))  # Create a figure and axis

# Plots by month
ax.plot(months, avg_percentage_by_month['CLEMENCEAU'], label='CLEMENCEAU')
ax.plot(months, avg_percentage_by_month['TREMOUILLE'], label='TREMOUILLE')
ax.plot(months, avg_percentage_by_month['MONGE'], label='MONGE')

# Add Value Labels
addlabels(months, avg_percentage_by_month['CLEMENCEAU'])
addlabels(months, avg_percentage_by_month['TREMOUILLE'])
addlabels(months, avg_percentage_by_month['MONGE'])

ax.set_title('Parking Percentage by month')
ax.set_xlabel('Months')
ax.set_ylabel('Percentage')

# Add Legend
ax.legend()

# Add grid
plt.grid()

# Replace Negative Percentage
def replace_negatives(x):
    if x < 0:
        return 0
    else:
        return x

df['pourcentage'] = df['pourcentage'].apply(replace_negatives)

# Visualise % data for parkings
fig, ax = plt.subplots(figsize=(16, 6))  # Create a figure and axis

# Plots
ax.plot(clem['datetime'], clem['pourcentage'], label='CLEMENCEAU')
ax.plot(tremo['datetime'], tremo['pourcentage'], label='TREMOUILLE')
ax.plot(tremo['datetime'], monge['pourcentage'], label='MONGE')

# Title and Labels
ax.set_title('Parking Percentage')
ax.set_xlabel('Date')
ax.set_ylabel('Percentage')

# Add Legend
ax.legend()

# Change X ticks
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Add grid
plt.grid()
plt.show()
