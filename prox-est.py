# Applying proximity-based logic for estimating contaminants based on likely regions for high contamination
import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2
import time

#keep track of execution time
start_time = time.time()

#defining high contamination districts
high_lead_cities = ['Lucknow', 'Jodhpur', 'Patna', 'Aurangabad', 'Darbhanga', 'Kolkata', 'New Delhi', 'Hyderabad', 'Chennai', 'Indore', 'Bijapur', 'Raipur', 'Durg']
high_cadmium_cities = ['Saharanpur', 'Bathinda', 'Samastipur', 'Bikaner', 'Alwar']
high_chromium_cities = ['Kanpur', 'Vellore', 'Durg', 'Cuttack']
high_arsenic_cities = ['Nadia', 'Murshidabad', 'Aligarh', 'Darrang', 'North 24 Parganas']
high_mercury_cities = ['Panipat', 'Bhopal', 'Singrauli', 'Krishna', 'Puri']
high_urban_waste_cities = ['Mumbai City', 'New Delhi', 'Kolkata', 'Chennai', 'Thane', 'North 24 Parganas', 'South 24 Parganas', 'Bangalore Urban', 'Ernakulam', 'Howrah', 'Ghaziabad', 'Hyderabad']
high_pesticide_cities = ['Sangrur', 'Thanjavur', 'Meerut', 'Buldhana', 'Kurnool']
high_ewaste_cities = ['Mumbai City', 'Pune', 'Thane', 'New Delhi', 'Bangalore Urban', 'Chennai', 'Gurgaon']
high_nuclear_cities = ['Anand']

# Load cities from CSV file
cities_df = pd.read_csv('cities.csv')
cities = cities_df['City'].tolist()

#define a function to calculate distance between 2 cities, the latitude and longitude of which are given
def distance(city1, city2):
    if city1 not in cities_df['City'].values or city2 not in cities_df['City'].values:
        raise ValueError(f"One or both cities not found in the DataFrame: {city1}, {city2}")

    lat1 = cities_df.loc[cities_df['City'] == city1].iloc[0]['Latitude']
    lon1 = cities_df.loc[cities_df['City'] == city1].iloc[0]['Longitude']
    lat2 = cities_df.loc[cities_df['City'] == city2].iloc[0]['Latitude']
    lon2 = cities_df.loc[cities_df['City'] == city2].iloc[0]['Longitude']

    # Convert degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Calculate the distance using the Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance_km = 6371 * c  # Radius of Earth in kilometers
    return distance_km


# Assign high, medium, low contaminant levels based on distance from these hotspots
def estimate_contaminant(city, hotspots, high_range, medium_range, low_range):
    
    distances = [distance(city, hotspot) for hotspot in hotspots]
    min_distance = min(distances)
    
    if min_distance <= 25:
        return np.random.uniform(*high_range)
    elif min_distance <= 300:
        return np.random.uniform(*medium_range)
    else:
        return np.random.uniform(*low_range)
    
# Defining probable ranges based on likely proximity to contamination levels (high, medium, low exposure)(can be tweaked)
ranges = {
    'Lead (ppm)': ((200, 300), (50, 200), (10, 50)), 'Cadmium (ppm)': ((20, 50), (5, 20), (0.1, 5)),
    'Chromium (ppm)': ((150, 200), (50, 150), (5, 50)), 'Arsenic (ppm)': ((20, 50), (5, 20), (0.5, 5)),
    'Mercury (ppm)': ((5, 10), (1, 5), (0.01, 1)), 'Urban Waste (kg/m²)': ((50, 100), (10, 50), (0.1, 10)),
    'Excessive Pesticides (ppm)': ((2, 5), (0.5, 2), (0, 0.5)), 'E-waste (kg/m²)': ((10, 15), (2, 10), (0.05, 2)),
    'Nuclear Waste (Bq/kg)': ((0.5, 1), (0.1, 0.5), (0.001, 0.1))
}

# Create DataFrame object
df = pd.DataFrame()

# Estimate based on proximity to contaminant hotspots for each city and write into the dataframe
df['City'] = cities
df['Lead (ppm)'] = [round(estimate_contaminant(city, high_lead_cities, *ranges['Lead (ppm)']), 0) for city in cities]
df['Cadmium (ppm)'] = [round(estimate_contaminant(city, high_cadmium_cities, *ranges['Cadmium (ppm)']), 1) for city in cities]
df['Chromium (ppm)'] = [round(estimate_contaminant(city, high_chromium_cities, *ranges['Chromium (ppm)']), 1) for city in cities]
df['Arsenic (ppm)'] = [round(estimate_contaminant(city, high_arsenic_cities, *ranges['Arsenic (ppm)']), 1) for city in cities]
df['Mercury (ppm)'] = [round(estimate_contaminant(city, high_mercury_cities, *ranges['Mercury (ppm)']), 2) for city in cities]
df['Urban Waste (kg/m²)'] = [round(estimate_contaminant(city, high_urban_waste_cities, *ranges['Urban Waste (kg/m²)']), 1) for city in cities]
df['Excessive Pesticides (ppm)'] = [round(estimate_contaminant(city, high_pesticide_cities, *ranges['Excessive Pesticides (ppm)']), 1) for city in cities]
df['E-waste (kg/m²)'] = [round(estimate_contaminant(city, high_ewaste_cities, *ranges['E-waste (kg/m²)']), 2) for city in cities]
df['Nuclear Waste (Bq/kg)'] = [round(estimate_contaminant(city, high_nuclear_cities, *ranges['Nuclear Waste (Bq/kg)']), 3) for city in cities]

# Save updated DataFrame as CSV
proximity_csv_path = "pollution-estimation.csv"
df.to_csv(proximity_csv_path, index=False)

print(f"Proximity-based estimation complete. Data saved to {proximity_csv_path}")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")