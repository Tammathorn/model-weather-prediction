#Label mapping
import json
from sklearn.preprocessing import LabelEncoder

# 1. Load the dataset
df = pd.read_csv('GlobalWeatherRepository.csv')

# 2. Define categorical columns to encode
categorical_cols = ['country', 'location_name', 'timezone', 'condition_text', 'wind_direction', 'moon_phase']

# Dictionary to store the mapping for each column
label_mappings = {}

# 3. Process each categorical column
for col in categorical_cols:
    le = LabelEncoder()
    # Fit and transform the data
    df[col] = le.fit_transform(df[col].astype(str))
    
    # Extract the mapping (index to class label)
    mapping = {int(index): label for index, label in enumerate(le.classes_)}
    
    # Store it in the main dictionary
    label_mappings[col] = mapping

# 4. Save the mappings to a JSON file
with open('label_mappings.json', 'w', encoding='utf-8') as file:
    json.dump(label_mappings, file, ensure_ascii=False, indent=4)

print("Dictionary saved successfully as 'label_mappings.json'")

# Display a sample of the mapping (top 5 countries)
print("\nSample mapping for top 5 countries:")
sample_countries = dict(list(label_mappings['country'].items())[:5])
print(sample_countries)
