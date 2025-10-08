import corella
import sys
import pandas as pd

input = int(sys.argv[1])

df = pd.DataFrame({
    'name': ['Eolophus roseicapilla', 'Eolophus roseicapilla'],
    'latitude': [-35.310, -35.273],
    'longitude': [149.125, 149.133],
    'place': ['a big tree', 'an open field'],
})

if input == 1:
    print(df)
    sys.exit()

if input == 2:
    df = corella.set_coordinates(dataframe=df,
                                 decimalLatitude = 'place', # wrong column
                                 decimalLongitude = 'longitude')
    sys.exit()

df = pd.DataFrame({
    'decimalLatitude': [-35.310, "-35.273"], # deliberate error for demonstration purposes
    'decimalLongitude': [149.125, 149.133],
    'date': ["14-01-2023", "15-01-2023"],
    'individualCount': [0, 2],
    'scientificName': ["Callocephalon fimbriatum", "Eolophus roseicapilla"],
    'country': ["AU", "AU"],
    'occurrenceStatus': ["present", "present"],
})

if input == 3:
    corella.check_dataset(occurrences=df)
    sys.exit()