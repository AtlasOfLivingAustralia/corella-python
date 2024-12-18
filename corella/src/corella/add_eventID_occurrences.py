from .common_functions import check_for_dataframe

def add_eventID_occurrences(occurrences=None,
                            events=None,
                            eventType=None):
    
    # check for dataframes
    check_for_dataframe(dataframe=occurrences,func='add_eventID_occurrences')
    check_for_dataframe(dataframe=events,func='add_eventID_occurrences')

    if 'occurrenceID' not in occurrences.columns:
        raise ValueError("Please add occurrence IDs before adding eventIDs")
    
    if eventType is None:
        raise ValueError("Please specify which type of event should be associated with the occurrence (i.e. Observation)")   

    occurrences.insert(1,'eventID',['' for i in list(range(occurrences.shape[0]))])
    
    for i,row in occurrences.iterrows():
        if any(events['eventDate'].astype(str).str.contains(str(row['eventDate'].date()))):
            temp = events[events['eventDate'].astype(str).str.contains(str(row['eventDate'].date()))]
            indices = temp[temp['eventType'] == eventType].index
            if len(indices) > 1:
                raise ValueError("You have duplicate events.  Please check your events")
            else:
                index = indices[0]
            occurrences.at[i,'eventID'] = temp[temp['eventType'] == eventType]['eventID'][index]

    return occurrences