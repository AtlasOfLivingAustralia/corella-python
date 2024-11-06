import pandas as pd
import datetime
from .check_eventDate import check_eventDate

def use_datetime(dataframe=None,
                 eventDate=None,
                 year=None,
                 month=None,
                 day=None,
                 time=None,
                 string_to_datetime=False,
                 orig_format='%d-%m-%Y'):
        """
        Checks for time information, such as the date an occurrence occurred.  Also runs checks 
        on the validity of the format of the date.

        Parameters
        ----------
            eventDate: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the date of the occurrences.
            year: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the year of the occurrence.
            month: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the date of the occurrences.
            day: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the day of the occurrences.
            time: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the time of the occurrences.
            string_to_datetime: ``logical``
                An argument that tells ``galaxias`` to convert dates that are in a string format 
                to a ``datetime`` format.  Default is ``False``.
            orig_format: ``str``
                A string denoting the original format of the dates that are being converted from a 
                string to a ``datetime`` object.  Default is ``'%d-%m-%Y'``.

        Returns
        -------
            Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
        """

        if all([v is None for v in [eventDate,year,month,day,time]]):
            raise ValueError("No Darwin Core arguments supplied to `use_datetime()`.  See dir(self.use_datetime()) for valid arguments.")

        # create a temporary occurrences variable
        temp_occurrences = dataframe
        # create a dictionary of names for renaming
        names = {}

        for var in [eventDate,year,month,day,time]:
            if var is not None and var is eventDate:
                names[var.name] = 'eventDate'
            elif var is not None and var is year:
                names[var.name] = 'year'
            elif var is not None and var is month:
                names[var.name] = 'month'
            elif var is not None and var is day:
                names[var.name] = 'day'
            elif var is not None and var is time:
                names[var.name] = 'time'
            else:
                pass

        # check name of columns
        for var in [eventDate,year,month,day,time]:
            if var is not None:        
                if type(var) is datetime.datetime:
                    pass
                elif type(var) is pd.core.series.Series:
                    temp_occurrences = temp_occurrences.rename(columns={var.name: names[var.name]})
                else:
                    raise ValueError("only accepts datetime data types or pandas series as eventDate")

        # options to convert strings to datetime
        if string_to_datetime:
            for i,entry in enumerate(temp_occurrences['eventDate']):
                temp_occurrences['eventDate'][i] = datetime.datetime.strptime(entry,orig_format)

        # check format
        check_eventDate(dataframe=temp_occurrences)
        
        # assign updated occurrences to object
        return temp_occurrences