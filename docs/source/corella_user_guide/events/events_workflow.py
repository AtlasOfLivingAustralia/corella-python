import corella
import pandas as pd
import sys
import datetime

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

# temp_emof = my_dwca.emof.rename(
#     columns = {
#         "measurement": "measurementType",
#         "value": "measurementValue",
#         "unit": "measurementUnit",
#         "error": "measurementAccuracy"
#     }
# )