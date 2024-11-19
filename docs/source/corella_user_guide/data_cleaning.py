import corella
import pandas as pd
import sys

# set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# get arguments
stop = int(sys.argv[1])

# data
df = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
                   'latitude': [-35.310, '-35.273'], 
                   'longitude': [149.125, 149.133], 
                   'date': ['14-01-2023', '15-01-2023'], 
                   'status': ['present', 'present']})

# -----------------------------------------------------------------------------
# use_occurrences
# -----------------------------------------------------------------------------
if stop == 1:
    print(corella.use_occurrences(dataframe=df))
    sys.exit()

if stop == 2:
    print(corella.suggest_workflow(dataframe=df))
    sys.exit()

if stop == 3:
    print(corella.use_occurrences(dataframe=df))
    sys.exit()

if stop == 4:
    print(corella.use_occurrences(dataframe=df,basisOfRecord='observe'))
    sys.exit()

if stop == 5:
    print(corella.use_occurrences(dataframe=df,basisOfRecord='HumanObservation'))
    sys.exit()

if stop == 6:
    print(corella.use_occurrences(dataframe=df,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='status'))
    sys.exit()
    
if stop == 7:
    print(corella.use_occurrences(dataframe=df,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='status',
                                  occurrenceID=True))
    sys.exit()
    
if stop == 8:
    df = corella.use_occurrences(dataframe=df,
                                 basisOfRecord='HumanObservation',
                                 occurrenceStatus='status',
                                 occurrenceID=True)
    print(corella.check_data(occurrences=df))
    sys.exit()

if stop == 9:
    df = corella.use_occurrences(dataframe=df,
                                 basisOfRecord='HumanObservation',
                                 occurrenceStatus='status',
                                 occurrenceID=True)
    print(corella.suggest_workflow(dataframe=df))

# -----------------------------------------------------------------------------
# use_scientific_name
# -----------------------------------------------------------------------------
if stop == 10:
    print(corella.use_scientific_name(dataframe=df))
    sys.exit() 

if stop == 11:
    print(corella.use_scientific_name(dataframe=df,
                                      scientificName='species'))
    sys.exit() 

if stop == 12:
    df = corella.use_scientific_name(dataframe=df,
                                     scientificName='species')
    print(corella.check_data(occurrences=df))
    sys.exit() 

if stop == 13:
    df = corella.use_scientific_name(dataframe=df,
                                     scientificName='species')
    print(corella.suggest_workflow(dataframe=df))
    sys.exit() 

# -----------------------------------------------------------------------------
# use_coordinates
# -----------------------------------------------------------------------------
if stop == 14:
    print(corella.use_coordinates(dataframe=df))
    sys.exit() 

if stop == 15:
    print(corella.use_coordinates(dataframe=df,
                                  decimalLatitude='latitude',
                                  decimalLongitude='longitude'))
    sys.exit() 

if stop == 16:
    df['latitude'] = pd.to_numeric(df['latitude'])
    print(corella.use_coordinates(dataframe=df,
                                  decimalLatitude='latitude',
                                  decimalLongitude='longitude'))
    sys.exit() 

if stop == 17:
    df['latitude'] = pd.to_numeric(df['latitude'])
    print(corella.use_coordinates(dataframe=df,
                                  decimalLatitude='latitude',
                                  decimalLongitude='longitude',
                                  geodeticDatum='WGS84'))
    sys.exit() 

if stop == 18:
    df['latitude'] = pd.to_numeric(df['latitude'])
    print(corella.use_coordinates(dataframe=df,
                                  decimalLatitude='latitude',
                                  decimalLongitude='longitude',
                                  geodeticDatum='WGS84',
                                  coordinatePrecision=0.1))
    sys.exit() 

if stop == 19:
    df['latitude'] = pd.to_numeric(df['latitude'])
    df = corella.use_coordinates(dataframe=df,
                                 decimalLatitude='latitude',
                                 decimalLongitude='longitude',
                                 geodeticDatum='WGS84',
                                 coordinatePrecision=0.1)
    print(corella.check_data(occurrences=df))
    sys.exit() 

if stop == 20:
    df['latitude'] = pd.to_numeric(df['latitude'])
    df = corella.use_coordinates(dataframe=df,
                                 decimalLatitude='latitude',
                                 decimalLongitude='longitude',
                                 geodeticDatum='WGS84',
                                 coordinatePrecision=0.1)
    print(corella.suggest_workflow(dataframe=df))
    sys.exit() 

# -----------------------------------------------------------------------------
# use_coordinates
# -----------------------------------------------------------------------------
if stop == 21:
    print(corella.use_datetime(dataframe=df))
    sys.exit() 

if stop == 22:
    print(corella.use_datetime(dataframe=df,
                               eventDate='date'))
    sys.exit() 

if stop == 23:
    print(corella.use_datetime(dataframe=df,
                               eventDate='date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True))
    sys.exit() 

if stop == 24:
    df = corella.use_datetime(dataframe=df,
                               eventDate='date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    print(corella.check_data(occurrences=df))
    sys.exit() 

if stop == 25:
    df = corella.use_datetime(dataframe=df,
                               eventDate='date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    print(corella.suggest_workflow(dataframe=df))
    sys.exit() 