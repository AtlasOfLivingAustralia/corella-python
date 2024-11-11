import datetime
from .common_functions import check_is_datetime,check_is_numeric

def check_datetime(dataframe=None,
                   errors=[]):
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

    # first, raise an error if there is not an eventDate column
    if 'eventDate' not in dataframe.columns:
        errors.append('eventDate is a required field. Please ensure it is in your dataframe')

    # accepted ranges for dates and times
    ranges_datetimes = {
        'eventDate': [datetime.datetime.fromtimestamp(0),datetime.datetime.now()],
        'year': [0,datetime.datetime.now().year],
        'month': [1,12],
        'day': [1,31],
        'eventTime': [datetime.datetime.fromtimestamp(0).time,datetime.datetime.now().time]
    }

    # check values 
    for var in ranges_datetimes.keys():

        # check if in columns
        if var in dataframe.columns:

            # check type of variable first
            if var in ['eventDate','eventTime']:
                errors = check_is_datetime(dataframe=dataframe,column_name=var,errors=errors)
            else:
                errors = check_is_numeric(dataframe=dataframe,column_name=var,errors=errors)
            
            # if the data type in column is correct, see if there are invalid values
            if not any(var in x for x in errors):
                valid_count = dataframe[var].between(ranges_datetimes[var][0], ranges_datetimes[var][1], inclusive='both').sum()
                if valid_count < len(dataframe[var]):
                    errors.append("There are some invalid {} values.  They should be between {} and {}.".format(var,ranges_datetimes[var][0],ranges_datetimes[var][1]))

    # return errors if there are any; else, return None if everything is ok  
    if errors is not None:
        return errors  
    return None