import datetime
import pandas as pd

def check_datetime(dataframe=None):
    """
    Checks whether or not your event dates complies with 
    Darwin Core standards.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    # First, check if a dataframe is provided
    if dataframe is None:
        raise ValueError("Please provide a dataframe to this function.")

    # accepted formats for inputs
    accepted_formats = {
        'eventDate': [datetime.datetime,pd._libs.tslibs.timestamps.Timestamp],
        'year': [int], 
        'month': [int],
        'day': [int],
        'eventTime': [datetime.datetime,pd._libs.tslibs.timestamps.Timestamp]
    }

    # accepted ranges for dates and times
    ranges_datetimes = {
        'eventDate': [datetime.datetime.fromtimestamp(0),datetime.datetime.now()],
        'year': [0,datetime.datetime.now().year],
        'month': [1,12],
        'day': [1,31],
        'eventTime': [datetime.datetime.fromtimestamp(0).time,datetime.datetime.now().time]
    }

    # first, raise an error if there is not an eventDate column
    if 'eventDate' not in dataframe.columns:
        raise ValueError('eventDate is a required field. Please ensure it is in your dataframe')

    errors = []

    # check values 
    for var in accepted_formats.keys():

        if var in dataframe.columns:
            column_types = list(set(list(type(x) for x in list(dataframe[var]))))
            if len(column_types) > 1:
                errors.append("There are multiple types in the {} column - ensure that there are only {} variable types".format(var,accepted_formats[var]))
            else:
                if column_types[0] not in accepted_formats[var]:
                    errors.append("The accepted type for the {} column is {}.  Yours is currently in {}.".format(var,accepted_formats[var],column_types))
                else:
                    valid_count = dataframe[var].between(ranges_datetimes[var][0], ranges_datetimes[var][1], inclusive='both').sum()

                    # return errors
                    if valid_count < len(dataframe[var]):
                        errors.append("There are some invalid {} values.  They should be between {} and {}.".format(var,ranges_datetimes[var][0],ranges_datetimes[var][1]))
            
    return errors