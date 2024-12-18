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
occ = pd.read_csv('corella_user_guide/data/occurrences_dwc.csv')

# -----------------------------------------------------------------------------
# use_occurrences
# -----------------------------------------------------------------------------
if stop == 1:
    print(corella.check_data(occurrences=occ))
    sys.exit()

if stop == 2:
    print(corella.suggest_workflow(occurrences=occ))
    sys.exit()

if stop == 3:
    print(corella.use_occurrences(dataframe=occ))
    sys.exit()

if stop == 5:
    print(corella.use_occurrences(dataframe=occ,
                                  basisOfRecord='HumanObservation'))
    sys.exit()

if stop == 6:
    print(corella.use_occurrences(dataframe=occ,
                                  basisOfRecord='HumanObservation',
                                  occurrenceID=True))
    sys.exit()

if stop == 7:
    print(corella.use_occurrences(dataframe=occ,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='PRESENT',
                                  occurrenceID=True))
    sys.exit()
    
if stop == 8:
    occ = corella.use_occurrences(dataframe=occ,
                                 basisOfRecord='HumanObservation',
                                 occurrenceStatus='PRESENT',
                                 occurrenceID=True)
    print(corella.check_data(occurrences=occ))
    sys.exit()

if stop == 9:
    occ = corella.use_occurrences(dataframe=occ,
                                 basisOfRecord='HumanObservation',
                                 occurrenceStatus='PRESENT',
                                 occurrenceID=True)
    print(corella.suggest_workflow(occurrences=occ))

# -----------------------------------------------------------------------------
# use_scientific_name
# -----------------------------------------------------------------------------
if stop == 10:
    print(corella.use_scientific_name(dataframe=occ))
    sys.exit() 

if stop == 11:
    print(corella.use_scientific_name(dataframe=occ,
                                      scientificName='Species'))
    sys.exit() 

if stop == 12:
    occ = corella.use_scientific_name(dataframe=occ,
                                     scientificName='Species')
    print(corella.check_data(occurrences=occ))
    sys.exit() 

if stop == 13:
    occ = corella.use_scientific_name(dataframe=occ,
                                     scientificName='Species')
    print(corella.suggest_workflow(occurrences=occ))
    sys.exit() 

# -----------------------------------------------------------------------------
# use_coordinates
# -----------------------------------------------------------------------------
if stop == 14:
    print(corella.use_coordinates(dataframe=occ))
    sys.exit() 

if stop == 15:
    print(corella.use_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude'))
    sys.exit() 

if stop == 16:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    print(corella.use_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude'))
    sys.exit() 

if stop == 17:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    print(corella.use_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude',
                                  geodeticDatum='WGS84'))
    sys.exit() 

if stop == 18:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    print(corella.use_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude',
                                  geodeticDatum='WGS84',
                                  coordinatePrecision=0.1))
    sys.exit() 

if stop == 19:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    occ = corella.use_coordinates(dataframe=occ,
                                 decimalLatitude='Latitude',
                                 decimalLongitude='Longitude',
                                 geodeticDatum='WGS84',
                                 coordinatePrecision=0.1)
    print(corella.check_data(occurrences=occ))
    sys.exit() 

if stop == 20:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    occ = corella.use_coordinates(dataframe=occ,
                                 decimalLatitude='Latitude',
                                 decimalLongitude='Longitude',
                                 geodeticDatum='WGS84',
                                 coordinatePrecision=0.1)
    print(corella.suggest_workflow(occurrences=occ))
    sys.exit() 

# -----------------------------------------------------------------------------
# use_datetime
# -----------------------------------------------------------------------------
if stop == 21:
    print(corella.use_datetime(dataframe=occ))
    sys.exit() 

if stop == 22:
    print(corella.use_datetime(dataframe=occ,
                               eventDate='Collection_date'))
    sys.exit() 

if stop == 23:
    print(corella.use_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True))
    sys.exit() 

if stop == 24:
    occ = corella.use_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    print(corella.check_data(occurrences=occ))
    sys.exit() 

if stop == 25:
    occ = corella.use_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    print(corella.suggest_workflow(occurrences=occ))
    sys.exit() 

# -----------------------------------------------------------------------------
# use_abundance
# -----------------------------------------------------------------------------
occ = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
                   'latitude': [-35.310, '-35.273'], 
                   'longitude': [149.125, 149.133], 
                   'date': ['14-01-2023', '15-01-2023'], 
                   'status': ['present', 'present'],
                   'count': [2,1]})

if stop == 26:
    print(corella.use_abundance(dataframe=occ))
    sys.exit() 

if stop == 27:
    print(corella.use_abundance(dataframe=occ,individualCount='count'))
    sys.exit() 

# -----------------------------------------------------------------------------
# use_abundance
# -----------------------------------------------------------------------------
occ = pd.read_csv('corella_user_guide/data/occurrences_dwc.csv')

if stop == 28:
    print(corella.use_locality(dataframe=occ))
    sys.exit() 

if stop == 29:
    print(corella.use_locality(dataframe=occ,continent='Australia'))
    sys.exit() 

if stop == 30:
    print(corella.use_locality(dataframe=occ,continent='Oceania',country='Australia'))
    sys.exit() 

# -----------------------------------------------------------------------------
# final
# -----------------------------------------------------------------------------
occ = pd.read_csv('corella_user_guide/data/occurrences_dwc.csv')

if stop == 31:
    occ = corella.use_occurrences(dataframe=occ,basisOfRecord='HumanObservation',
                                occurrenceStatus='PRESENT',occurrenceID=True)
    occ = corella.use_scientific_name(dataframe=occ,scientificName='Species')
    occ = corella.use_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude',
                                  geodeticDatum='WGS84',
                                  coordinatePrecision=0.1)
    occ = corella.use_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    print(corella.check_data(occurrences=occ))
    import sys
    sys.exit()