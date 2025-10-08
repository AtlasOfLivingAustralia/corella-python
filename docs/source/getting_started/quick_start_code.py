import corella
import sys
import pandas as pd

input = int(sys.argv[1])

df = pd.DataFrame({
    'latitude': [-35.310, "-35.273"], # deliberate error for demonstration purposes
    'longitude': [149.125, 149.133],
    'date': ["14-01-2023", "15-01-2023"],
    'time': ["10:23:00", "11:25:00"],
    'month': ["January", "February"],
    'day': [100, 101],
    'species': ["Callocephalon fimbriatum", "Eolophus roseicapilla"],
    'n': [2, 3],
    'crs': ["WGS84", "WGS8d"],
    'country': ["Australia", "Denmark"],
    'continent': ["Oceania", "Europe"]})

if input == 1:
    print(df)
    sys.exit()

if input == 2:
    df_dwc = corella.set_scientific_name(dataframe=df,scientificName='species')
    print(df_dwc)
    sys.exit()

if input == 3:
    df_dwc = corella.set_scientific_name(dataframe=df,scientificName='species')
    df_dwc = corella.set_coordinates(dataframe=df_dwc,
                                     decimalLongitude = 'longitude',
                                     decimalLatitude = 'latitude')



if input == 4:
    df_dwc = corella.set_scientific_name(dataframe=df,scientificName='species')
    df_dwc['latitude'] = pd.to_numeric(df_dwc['latitude'])
    df_dwc = corella.set_coordinates(dataframe=df_dwc,
                                    decimalLongitude = 'longitude',
                                    decimalLatitude = 'latitude',
                                    )
    print(df_dwc)
    sys.exit()

if input == 5:
    corella.suggest_workflow(occurrences=df)
    sys.exit()

if input == 6:
    df_edited = corella.set_occurrences(occurrences=df,
                                        occurrenceID='sequential',
                                        basisOfRecord='HumanObservation')
    corella.suggest_workflow(occurrences=df_edited)
    sys.exit()

if input == 7:
    df = pd.DataFrame({
        'latitude': [-35.310, "-35.273"], # deliberate error for demonstration purposes
        'longitude': [149.125, 149.133],
        'date': ["14-01-2023", "15-01-2023"],
        'individualCount': [0, 2],
        'species': ["Callocephalon fimbriatum", "Eolophus roseicapilla"],
        'country': ["AU", "AU"],
        'occurrenceStatus': ["present", "present"],
    })
    corella.check_dataset(occurrences=df)
    sys.exit()