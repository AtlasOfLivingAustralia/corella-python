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

if stop == 1:
    print(corella.use_occurrences(dataframe=df))
    sys.exit()

if stop == 2:
    print(corella.use_occurrences(dataframe=df,basisOfRecord='observe'))
    sys.exit()

if stop == 3:
    print(corella.use_occurrences(dataframe=df,basisOfRecord='HumanObservation'))
    sys.exit()

if stop == 4:
    print(corella.use_occurrences(dataframe=df,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='status'))
    sys.exit()
    
if stop == 5:
    print(corella.use_occurrences(dataframe=df,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='status',
                                  occurrenceID=True))
    sys.exit()
    
df = corella.use_occurrences(dataframe=df,
                             basisOfRecord='HumanObservation',
                             occurrenceStatus='status',
                             occurrenceID=True)

if stop == 6:
    print(corella.check_data(occurrences=df))
    sys.exit()

if stop == 7:
    print(corella.suggest_workflow(dataframe=df))