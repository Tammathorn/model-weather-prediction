#Cleaning Data
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv('GlobalWeatherRepository.csv')

# Drop redundant data
# Using Celsius, km/h, mm 
# Drop Fahrenheit, mph, inches and epoch time
cols_to_drop = [
    'temperature_fahrenheit', 
    'wind_mph', 
    'pressure_in', 
    'precip_in', 
    'feels_like_fahrenheit', 
    'visibility_miles', 
    'gust_mph',
    'last_updated_epoch' 
]
df = df.drop(columns=cols_to_drop)

# Datetime Features
df['last_updated'] = pd.to_datetime(df['last_updated'])
df['year'] = df['last_updated'].dt.year
df['month'] = df['last_updated'].dt.month
df['day'] = df['last_updated'].dt.day
df['hour'] = df['last_updated'].dt.hour
df = df.drop(columns=['last_updated'])

# Categorical Data Handling
categorical_cols = ['country', 'location_name', 'timezone', 'condition_text', 'wind_direction', 'moon_phase']
le = LabelEncoder()

for col in categorical_cols:
    df[col] = le.fit_transform(df[col].astype(str))

# Drop complex time columns
complex_time_cols = ['sunrise', 'sunset', 'moonrise', 'moonset']
df = df.drop(columns=complex_time_cols)

# Define Features (X) and Target (y) for PM 2.5 Prediction
X_pm = df.drop(columns=['air_quality_PM2.5'])
y_pm = df['air_quality_PM2.5']

# Define Features (X) and Target (y) for Temperature Prediction
X_temp = df.drop(columns=['temperature_celsius']) 
y_temp = df['temperature_celsius']

# Save
df.to_csv('Cleaned_Weather_Data.csv', index=False)