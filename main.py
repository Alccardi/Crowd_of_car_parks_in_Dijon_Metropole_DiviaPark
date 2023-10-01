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

parking_list = ['CLEMENCEAU', 'CONDORCET', 'DARCY', 'DAUPHINE', 'GRANGIER', 'MALRAUX', 'MONGE', 'SAINTE-ANNE', 'TIVOLI', 'TREMOUILLE']

# Replace Negative Percentage
def replace_negatives(x):
    if x < 0:
        return 0
    else:
        return x

df['pourcentage'] = df['pourcentage'].apply(replace_negatives)

# Filter data for CLEMENCEAU and TREMOUILLE
clem = df[df['parking'] == 'CLEMENCEAU']
tremo = df[df['parking'] == 'TREMOUILLE']

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












