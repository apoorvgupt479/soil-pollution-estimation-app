import tkinter as tk
from tkinter import ttk
import csv

class DynamicDropdownApp:
    def update_value(self, event):
        # Get the selected value from the combobox
        self.city = self.citycombobox.get()
        print("Selected District:", self.city)
        
        # Read cities.csv and find the latitude and longitude for the selected city
        with open('cities.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['City'] == self.city:
                    latitude = row['Latitude']
                    longitude = row['Longitude']
                    population = row['Population']
                    area = row['Area (in km^2)']
                    
                    # Remove old city info
                    if hasattr(self, 'latitude_label'):
                        self.latitude_label.destroy()
                    if hasattr(self, 'longitude_label'):
                        self.longitude_label.destroy()
                    if hasattr(self, 'population_label'):
                        self.population_label.destroy()
                    if hasattr(self, 'area_label'):
                        self.area_label.destroy()
                    
                    # Display city info
                    self.latitude_label = ttk.Label(root, text=f"\nLatitude: {latitude}", background=root['background'])
                    self.latitude_label.pack()
                    self.longitude_label = ttk.Label(root, text=f"Longitude: {longitude}", background=root['background'])
                    self.longitude_label.pack()
                    self.population_label = ttk.Label(root, text=f"Population: {population}", background=root['background'])
                    self.population_label.pack()
                    self.area_label = ttk.Label(root, text=f"Area (in km²): {area}\n\n", background=root['background'])
                    self.area_label.pack()
        
        # Clear old pollution labels
        for label in self.pollution_labels:
            label.destroy()
        self.pollution_labels.clear()
        
        # Open the pollution estimation file and display details for the selected city
        with open('pollution-estimation.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['City'] == self.city:
                    # Display pollution details for the selected city
                    for key, value in row.items():
                        if key != "City":
                            label = ttk.Label(root, text=f"{key}: {value}", background=root['background'])
                            label.pack()
                            self.pollution_labels.append(label)
                    break

    def __init__(self, root):
        # Create a label for the dropdown box
        label = ttk.Label(root, text="Select District", background=root['background'])
        label.pack()

        # Initialize pollution labels list
        self.pollution_labels = []

        # Read cities.csv and get all the cities
        cities = []
        with open('cities.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cities.append(row['City'])

        # Sort the cities alphabetically
        cities.sort()

        # Create a combobox with the sorted cities as options
        self.citycombobox = ttk.Combobox(root, values=cities)
        self.citycombobox.pack()

        # Bind the update_value method to the combobox selection event
        self.citycombobox.bind("<<ComboboxSelected>>", self.update_value)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Soil Pollution Estimation App")
    root.minsize(width=300, height=350)
    app = DynamicDropdownApp(root)
    root.mainloop()
