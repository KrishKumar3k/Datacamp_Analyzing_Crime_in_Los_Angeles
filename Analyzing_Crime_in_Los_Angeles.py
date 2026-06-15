#Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})

# Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour
crimes["HOUR"] = crimes["TIME OCC"].astype(str).str[:2].astype(int)
peak_crime_hour = crimes["HOUR"].value_counts().idxmax()
print(peak_crime_hour)

# Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? Save as a string variable called peak_night_crime_location.
crimes["TIME OCC"] = crimes["TIME OCC"].astype(int)
night_crimes = crimes[(crimes["TIME OCC"] >= 2200) | (crimes["TIME OCC"] < 400)]
peak_night_crime_location = night_crimes["AREA NAME"].value_counts().idxmax()
print(peak_night_crime_location)

# Identify the number of crimes committed against victims of different age groups. Save as a pandas Series called victim_ages, with age group labels "0-17", "18-25", "26-34", "35-44", "45-54", "55-64", and "65+" as the index and the frequency of crimes as the values.
age_bins = [0, 17, 25, 34, 44, 54, 64, 120]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
victim_ages = pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels).value_counts().sort_index()
print(victim_ages)