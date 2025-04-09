import corella
import pandas as pd
import sys

# get option
stopping_point = sys.argv[1]
if len(sys.argv) > 1:
    data_type = True #sys.argv[2]
else:
    data_type = False

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# --------------------------------------------------------
# Part 1
# --------------------------------------------------------

# read in data
events=pd.read_csv("corella_user_guide/data/events_use.csv")
occ=pd.read_csv("corella_user_guide/data/occurrences_event_nomulti.csv")

# generate initial data report and exit
if stopping_point == "1":
    corella.check_dataset(occurrences=occ,events=events)
    sys.exit()

if stopping_point == "2":
    corella.suggest_workflow(occurrences=occ,events=events)
    sys.exit()

# --------------------------------------------------------
# Use events
# --------------------------------------------------------

if stopping_point == "4":
    new_events = corella.set_events(dataframe=events,eventType='type',samplingProtocol='Observation',
                                    Event='name')
    print(new_events.head())
    sys.exit()

if stopping_point == "5":
    new_events = corella.set_events(dataframe=events,eventType='type',samplingProtocol='Observation',
                                    Event='name',event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"},
                                    random_id=True)
    print(new_events.head())
    sys.exit()

if stopping_point == "6":
    new_events = corella.set_events(dataframe=events,eventType='type',samplingProtocol='Observation',
                                    Event='name',event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"},
                                    random_id=True)
    corella.check_dataset(occurrences=occ,events=new_events)
    sys.exit()

if stopping_point == "7":
    new_events = corella.set_events(dataframe=events,eventType='type',samplingProtocol='Observation',
                                    Event='name',event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"},
                                    random_id=True)
    corella.suggest_workflow(occurrences=occ,events=new_events)
    sys.exit()

# --------------------------------------------------------
# set_datetime
# --------------------------------------------------------

if stopping_point == "8":
    new_events = corella.set_datetime(dataframe=events)
    print(new_events.head())
    sys.exit()

if stopping_point == "9":
    new_events = corella.set_datetime(dataframe=events,eventDate='date')
    print(new_events.head())
    sys.exit()

if stopping_point == "10":
    new_events = corella.set_datetime(dataframe=events,eventDate='date',
                                      string_to_datetime=True,yearfirst=False,dayfirst=True)
    print(new_events.head())
    sys.exit()

if stopping_point == "11":
    new_events = corella.set_datetime(dataframe=events,eventDate='date',
                                      string_to_datetime=True,yearfirst=False,dayfirst=True)
    corella.check_dataset(events=new_events)
    sys.exit()

if stopping_point == "12":
    new_events = corella.set_datetime(dataframe=events,eventDate='date',
                                      string_to_datetime=True,yearfirst=False,dayfirst=True)
    corella.suggest_workflow(events=new_events)
    sys.exit()

if stopping_point == "13":
    new_events = corella.set_events(dataframe=events,eventType='type',samplingProtocol='Observation',
                                Event='name',event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"},
                                random_id=True)
    new_events = corella.set_datetime(dataframe=new_events,eventDate='date',string_to_datetime=True,
                                  yearfirst=False,dayfirst=True)
    new_occ = corella.set_scientific_name(dataframe=occ,scientificName='Species')
    new_occ = corella.set_coordinates(dataframe=new_occ,decimalLatitude='Latitude',decimalLongitude='Longitude',
                                  geodeticDatum='WGS84',coordinatePrecision=0.1)
    new_occ = corella.set_datetime(dataframe=new_occ,eventDate='Collection_date',string_to_datetime=True,
                               yearfirst=False,dayfirst=True)
    new_occ = corella.set_occurrences(dataframe=new_occ,basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',
                                      occurrenceID=True,random_id=True,add_eventID=True,events=new_events,
                                      eventType='Observation')
    print(new_occ.head())
    sys.exit()

# --------------------------------------------------------
# set_abundance
# --------------------------------------------------------
if stopping_point == '14':
    occ = corella.set_abundance(dataframe=occ,individualCount='number_birds')
    print(occ.head())

# --------------------------------------------------------
# set_locality
# --------------------------------------------------------
if stopping_point == '15':
    events = corella.set_locality(dataframe=events,locality='location')
    print(events.head())

# --------------------------------------------------------
# Passing dataset
# --------------------------------------------------------

if stopping_point == "16":
    events = corella.set_events(dataframe=events,eventType='type',samplingProtocol='Observation',
                                Event='name',event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"},
                                random_id=True)
    events = corella.set_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,
                                  dayfirst=True)
    events = corella.set_locality(dataframe=events, locality='location')
    occ = corella.set_scientific_name(dataframe=occ,scientificName='Species')
    occ = corella.set_coordinates(dataframe=occ,decimalLatitude='Latitude',decimalLongitude='Longitude',
                                  geodeticDatum='WGS84',coordinatePrecision=0.1)
    occ = corella.set_datetime(dataframe=occ,eventDate='Collection_date',string_to_datetime=True,
                               yearfirst=False,dayfirst=True)
    occ = corella.set_occurrences(dataframe=occ,basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',
                                occurrenceID=True,add_eventID=True,events=events,eventType='Observation',
                                random_id=True)
    occ = corella.set_abundance(dataframe=occ,individualCount='number_birds')
    corella.check_dataset(occurrences=occ,events=events)
    import sys
    sys.exit()

# temp_emof = my_dwca.emof.rename(
#     columns = {
#         "measurement": "measurementType",
#         "value": "measurementValue",
#         "unit": "measurementUnit",
#         "error": "measurementAccuracy"
#     }
# )