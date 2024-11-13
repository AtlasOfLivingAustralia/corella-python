import datetime
import pandas as pd
from .check_datetime import check_datetime

def use_datetime(dataframe=None,
                 eventDate=None,
                 year=None,
                 month=None,
                 day=None,
                 eventTime=None,
                 string_to_datetime=False,
                 time_format='%H:%m:%S'):
    """
    Checks for time information, such as the date an occurrence occurred.  Also runs checks 
    on the validity of the format of the date.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        eventDate: ``str``
            A column name (``str``) denoting the column with the dates of the events, or a ``str`` or 
            ``datetime.datetime`` object denoting the date of the event.
        year: ``str`` or ``int``
            A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
            the year of the event.
        month: ``str`` or ``int``
            A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
            the month of the event.
        day: ``str`` or ``int``
            A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
            the day of the event.
        eventTime: ``str``
            A column name (``str``) denoting the column with the dates of the events, or a ``str`` denoting
            the time of the event.
        string_to_datetime: ``logical``
            An argument that tells ``corella`` to convert dates that are in a string format to a ``datetime`` 
            format.  Default is ``False``.
        orig_format: ``str``
            A ``str`` denoting the original format of the dates that are being converted from a ``str`` to a 
            ``datetime`` object.  Default is ``'%d-%m-%Y'``.

    Returns
    -------
        Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
    """

    # raise a ValueError if no dataframe is provided
    if dataframe is None:
        raise ValueError('Please provide a dataframe.')

    # check for validating data
    if all([v is None for v in [eventDate,year,month,day,eventTime]]):
        if all ([v not in ['eventDate','year','month','day','eventTime'] for v in dataframe.columns]):
            raise ValueError("No Darwin Core arguments supplied to `use_datetime()`.  See dir(corella.use_datetime()) for valid arguments.")

    # mapping column names
    mapping = {
        eventDate: 'eventDate',
        year: 'year', 
        month: 'month',
        day: 'day',
        eventTime: 'eventTime'
    }

    # accepted formats for inputs
    accepted_formats = {
        eventDate: [datetime.datetime,str],
        year: [int], 
        month: [int],
        day: [int],
        eventTime: [datetime.datetime,str]
    }

    # check name of columns
    for var in mapping.keys():
        if var is not None:  
            if var not in dataframe.columns:      
                if type(var) in accepted_formats[var]:
                    dataframe[mapping[var]] = var
                    del mapping[var]
                else:
                    raise ValueError("Only a {} is accepted for {}".format(accepted_formats[var],var))
                
    # rename all necessary columns
    dataframe = dataframe.rename(columns=mapping)

    # add option to convert strings to datetime
    if string_to_datetime:
        dataframe['eventDate'] = pd.to_datetime(dataframe['eventDate'],yearfirst=True)
        if 'eventTime' in dataframe.columns:
            dataframe['eventTime'] = pd.to_datetime(dataframe['eventTime'],format=time_format).dt.time
    
    # check format
    errors = check_datetime(dataframe=dataframe,errors=[])
    
    # return errors if there are any; otherwise, return dataframe
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe