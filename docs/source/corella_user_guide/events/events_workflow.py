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
events=pd.read_csv("corella_user_guide/events/events_use.csv")
occ=pd.read_csv("corella_user_guide/events/occurrences_event_nomulti.csv")

# generate initial data report and exit
if stopping_point == "1":
    print(corella.check_data(occurrences=occ,events=events))
    sys.exit()

if stopping_point == "2":
    print(corella.suggest_workflow(occurrences=occ,events=events))
    sys.exit()

if stopping_point == "3":
    print(corella.use_events(dataframe=events))
    sys.exit()

if stopping_point == "4":
    print(corella.use_events(dataframe=events,
                             eventType='type',
                             samplingProtocol='Observation',
                             Event='name'))
    sys.exit()

if stopping_point == "5":
    print(corella.use_events(dataframe=events,
                             eventType='type',
                             samplingProtocol='Observation',
                             Event='name',
                             event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"}))
    sys.exit()

if stopping_point == "6":
    new_events = corella.use_events(dataframe=events,
                             eventType='type',
                             samplingProtocol='Observation',
                             Event='name',
                             event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    print(corella.check_data(occurrences=occ,events=new_events))
    sys.exit()

if stopping_point == "7":
    new_events = corella.use_events(dataframe=events,
                             eventType='type',
                             samplingProtocol='Observation',
                             Event='name',
                             event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    print(corella.suggest_workflow(events=new_events))
    sys.exit()

if stopping_point == "8":
    print(corella.use_datetime(dataframe=events))
    import sys
    sys.exit()

if stopping_point == "9":
    print(corella.use_datetime(dataframe=events,eventDate='date'))
    import sys
    sys.exit()

if stopping_point == "10":
    print(corella.use_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True))
    import sys
    sys.exit()

if stopping_point == "11":
    new_events = corella.use_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    corella.check_data(events=new_events)
    import sys
    sys.exit()

if stopping_point == "12":
    new_events = corella.use_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    corella.suggest_workflow(events=new_events)
    import sys
    sys.exit()

if stopping_point == "13":
    events = corella.use_events(dataframe=events,
                             eventType='type',
                             samplingProtocol='Observation',
                             Event='name',
                             event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    events = corella.use_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    occ = corella.use_occurrences(dataframe=occ,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='PRESENT',
                                  occurrenceID=True)
    occ = corella.use_scientific_name(dataframe=occ,
                                      scientificName='Species')
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
    print(corella.use_occurrences(dataframe=occ,add_eventID=True,events=events,eventType='Observation'))

if stopping_point == "14":
    events = corella.use_events(dataframe=events,
                             eventType='type',
                             samplingProtocol='Observation',
                             Event='name',
                             event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    events = corella.use_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    occ = corella.use_occurrences(dataframe=occ,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='PRESENT',
                                  occurrenceID=True,
                                  add_eventID=True,
                                  events=events,
                                  eventType='Observation')
    occ = corella.use_scientific_name(dataframe=occ,
                                      scientificName='Species')
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
    print(corella.check_data(occurrences=occ,events=events))


# temp_emof = my_dwca.emof.rename(
#     columns = {
#         "measurement": "measurementType",
#         "value": "measurementValue",
#         "unit": "measurementUnit",
#         "error": "measurementAccuracy"
#     }
# )