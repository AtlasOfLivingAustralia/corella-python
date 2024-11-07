import pandas as pd
import datetime
from .check_datetime import check_eventDate

def use_datetime(dataframe=None,
                 eventDate=None,
                 year=None,
                 month=None,
                 day=None,
                 eventTime=None,
                 string_to_date=False,
                 string_to_datetime=False,
                 orig_format_date='%d-%m-%Y',
                 orig_format_time='%h:%m:%s',
                 orig_format_datetime='%d-%m-%Y:%h:%m:%s'):
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

        if all([v is None for v in [eventDate,year,month,day,eventTime]]):
            raise ValueError("No Darwin Core arguments supplied to `use_datetime()`.  See dir(self.use_datetime()) for valid arguments.")

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
        for var in [eventDate,year,month,day,eventTime]:
            if var is not None:  
                if var not in dataframe.columns:      
                    if type(var) in accepted_formats[var]:
                        dataframe[mapping[var]] = var
                        del mapping[var]
                    else:
                        raise ValueError("Only a {} is accepted for {}".format(accepted_formats[var],var))

        # add option to convert strings to datetime
        if string_to_date:
            for i,entry in enumerate(dataframe['eventDate']):
                dataframe['eventDate'][i] = datetime.datetime.strptime(entry,orig_format_datetime)

        if string_to_datetime:
            if not string_to_date:
                for i,entry in enumerate(dataframe['eventDate']):
                    dataframe['eventDate'][i] = datetime.datetime.strptime(entry,orig_format_datetime)
            if 'eventTime' in dataframe.columns:
                for i,entry in enumerate(dataframe['eventTime']):
                    dataframe['eventTime'][i] = datetime.datetime.strptime(entry,orig_format_time)

        # check format
        check_eventDate(dataframe=dataframe)
        
        # assign updated occurrences to object
        return dataframe