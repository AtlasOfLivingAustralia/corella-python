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
# set_occurrences
# -----------------------------------------------------------------------------
if stop == 1:
    print(corella.check_dataset(occurrences=occ))
    sys.exit()

if stop == 2:
    print(corella.suggest_workflow(occurrences=occ))
    sys.exit()

if stop == 3:
    new_occ = corella.set_occurrences(dataframe=occ)
    print(new_occ.head())
    sys.exit()

if stop == 5:
    new_occ = corella.set_occurrences(dataframe=occ,basisOfRecord='HumanObservation')
    print(new_occ.head())
    sys.exit()

if stop == 6:
    new_occ = corella.set_occurrences(dataframe=occ,
                                      basisOfRecord='HumanObservation',
                                      occurrenceID=True,
                                      random_id=True)
    print(new_occ.head())
    sys.exit()

if stop == 7:
    new_occ = corella.set_occurrences(dataframe=occ,
                                      basisOfRecord='HumanObservation',
                                      occurrenceStatus='PRESENT',
                                      occurrenceID=True,
                                      random_id=True)
    print(new_occ.head())
    sys.exit()
    
if stop == 8:
    occ = corella.set_occurrences(dataframe=occ,
                                 basisOfRecord='HumanObservation',
                                 occurrenceStatus='PRESENT',
                                 occurrenceID=True,
                                 random_id=True)
    corella.check_dataset(occurrences=occ)
    sys.exit()

if stop == 9:
    occ = corella.set_occurrences(dataframe=occ,
                                 basisOfRecord='HumanObservation',
                                 occurrenceStatus='PRESENT',
                                 occurrenceID=True,
                                 random_id=True)
    corella.suggest_workflow(occurrences=occ)
    sys.exit()

# -----------------------------------------------------------------------------
# set_scientific_name
# -----------------------------------------------------------------------------
if stop == 10:
    print(corella.set_scientific_name(dataframe=occ))
    sys.exit() 

if stop == 11:
    print(corella.set_scientific_name(dataframe=occ,
                                      scientificName='Species'))
    sys.exit() 

if stop == 12:
    occ = corella.set_scientific_name(dataframe=occ,
                                     scientificName='Species')
    corella.check_dataset(occurrences=occ)
    sys.exit() 

if stop == 13:
    occ = corella.set_scientific_name(dataframe=occ,
                                     scientificName='Species')
    corella.suggest_workflow(occurrences=occ)
    sys.exit() 

# -----------------------------------------------------------------------------
# set_coordinates
# -----------------------------------------------------------------------------
if stop == 14:
    print(corella.set_coordinates(dataframe=occ))
    sys.exit() 

if stop == 15:
    print(corella.set_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude'))
    sys.exit() 

if stop == 16:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    print(corella.set_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude'))
    sys.exit() 

if stop == 17:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    print(corella.set_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude',
                                  geodeticDatum='WGS84'))
    sys.exit() 

if stop == 18:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    print(corella.set_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude',
                                  geodeticDatum='WGS84',
                                  coordinatePrecision=0.1))
    sys.exit() 

if stop == 19:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    occ = corella.set_coordinates(dataframe=occ,
                                 decimalLatitude='Latitude',
                                 decimalLongitude='Longitude',
                                 geodeticDatum='WGS84',
                                 coordinatePrecision=0.1)
    corella.check_dataset(occurrences=occ)
    sys.exit() 

if stop == 20:
    occ['Latitude'] = pd.to_numeric(occ['Latitude'],errors='coerce')
    occ = corella.set_coordinates(dataframe=occ,
                                 decimalLatitude='Latitude',
                                 decimalLongitude='Longitude',
                                 geodeticDatum='WGS84',
                                 coordinatePrecision=0.1)
    corella.suggest_workflow(occurrences=occ)
    sys.exit() 

# -----------------------------------------------------------------------------
# set_datetime
# -----------------------------------------------------------------------------
if stop == 21:
    print(corella.set_datetime(dataframe=occ))
    sys.exit() 

if stop == 22:
    print(corella.set_datetime(dataframe=occ,
                               eventDate='Collection_date'))
    sys.exit() 

if stop == 23:
    print(corella.set_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True))
    sys.exit() 

if stop == 24:
    occ = corella.set_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    corella.check_dataset(occurrences=occ)
    sys.exit() 

if stop == 25:
    occ = corella.set_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    corella.suggest_workflow(occurrences=occ)
    sys.exit() 

# -----------------------------------------------------------------------------
# set_abundance
# -----------------------------------------------------------------------------
occ = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
                   'latitude': [-35.310, '-35.273'], 
                   'longitude': [149.125, 149.133], 
                   'date': ['14-01-2023', '15-01-2023'], 
                   'status': ['present', 'present'],
                   'count': [2,1]})

if stop == 26:
    print(corella.set_abundance(dataframe=occ))
    sys.exit() 

if stop == 27:
    print(corella.set_abundance(dataframe=occ,individualCount='count'))
    sys.exit() 

# -----------------------------------------------------------------------------
# set_abundance
# -----------------------------------------------------------------------------
occ = pd.read_csv('corella_user_guide/data/occurrences_dwc.csv')

if stop == 28:
    print(corella.set_locality(dataframe=occ))
    sys.exit() 

if stop == 29:
    print(corella.set_locality(dataframe=occ,continent='Australia'))
    sys.exit() 

if stop == 30:
    print(corella.set_locality(dataframe=occ,continent='Oceania',country='Australia'))
    sys.exit() 

# -----------------------------------------------------------------------------
# set_taxonomy
# -----------------------------------------------------------------------------
if stop == 31:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ = corella.set_taxonomy(dataframe=occ,kingdom='Animalia',phylum='Chordata',taxon_class='Aves',
                               order='Psittaciformes',family='Cacatuidae',genus='Eolophus',
                               specificEpithet='roseicapilla',vernacularName='Galah')
    print(occ.head())
    sys.exit()

# -----------------------------------------------------------------------------
# set_collection
# -----------------------------------------------------------------------------
if stop == 32:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ = corella.set_collection(dataframe=occ,datasetID='b15d4952-7d20-46f1-8a3e-556a512b04c5',
                                 datasetName='Lacey Ctenomys Recaptures',catalogNumber='2008.1334')
    print(occ.head())
    sys.exit()

# -----------------------------------------------------------------------------
# set_individual_traits
# -----------------------------------------------------------------------------
if stop == 33:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ = corella.set_individual_traits(dataframe=occ,individualID=['123456','123457'],
                                        lifeStage='adult',sex=['male','female'],
                                        vitality='alive',reproductiveCondition='not reproductive')
    print(occ.head())
    sys.exit()
    
# -----------------------------------------------------------------------------
# set_license
# -----------------------------------------------------------------------------
if stop == 34:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ = corella.set_license(dataframe=occ,license=['CC-BY 4.0 (Int)', 'CC-BY-NC 4.0 (Int)'],
                              rightsHolder='The Regents of the University of California',
                              accessRights=['','not-for-profit use only'])
    print(occ.head())
    sys.exit()
    
# -----------------------------------------------------------------------------
# creating IDs
# -----------------------------------------------------------------------------
if stop == 35:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                        'latitude': [-35.310, -35.273], 
                        'longitude': [149.125, 149.133], 
                        'date': ['14-01-2023', '15-01-2023']})
    occ = corella.set_occurrences(dataframe=occ,occurrenceID=True,random_id=True)
    print(occ)
    sys.exit()

if stop == 36:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                        'latitude': [-35.310, -35.273], 
                        'longitude': [149.125, 149.133], 
                        'date': ['14-01-2023', '15-01-2023']})
    occ = corella.set_occurrences(dataframe=occ,occurrenceID=True,sequential_id=True)
    print(occ)
    sys.exit()

if stop == 37:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                        'latitude': [-35.310, -35.273], 
                        'longitude': [149.125, 149.133], 
                        'date': ['14-01-2023', '15-01-2023']})
    occ = corella.set_occurrences(dataframe=occ,occurrenceID=True,composite_id='date',sequential_id=True,add_sequential_id='first')
    print(occ)
    sys.exit()

if stop == 38:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                        'latitude': [-35.310, -35.273], 
                        'longitude': [149.125, 149.133], 
                        'date': ['14-01-2023', '15-01-2023']})
    occ = corella.set_occurrences(dataframe=occ,occurrenceID=True,composite_id='date',random_id=True,add_random_id='last')
    print(occ)
    sys.exit()

# -----------------------------------------------------------------------------
# final
# -----------------------------------------------------------------------------
occ = pd.read_csv('corella_user_guide/data/occurrences_dwc.csv')

if stop == 39:
    occ = corella.set_occurrences(dataframe=occ,basisOfRecord='HumanObservation',
                                occurrenceStatus='PRESENT',occurrenceID=True,random_id=True)
    occ = corella.set_scientific_name(dataframe=occ,scientificName='Species')
    occ = corella.set_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude',
                                  geodeticDatum='WGS84',
                                  coordinatePrecision=0.1)
    occ = corella.set_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    corella.check_dataset(occurrences=occ)
    sys.exit()