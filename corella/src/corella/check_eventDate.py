import numpy as np
import datetime

def check_eventDate(dataframe=None):
    """
    Checks whether or not your event dates complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    if 'eventDate' in dataframe.columns:

        eventDate_column = list(dataframe["eventDate"])
        types_edc = list(set(list(type(x) for x in eventDate_column)))
        if len(types_edc) > 1:
            raise ValueError("There are multiple types in the eventDate column - ensure that there are only datetime objects")
        else:
            if not isinstance(types_edc[0], datetime.datetime):
                if types_edc[0] is str:
                    raise ValueError("Data is not in datetime format.  If you want to convert from string to datetime object, set string_to_datetime to True.")
    else:
        raise ValueError("You need eventDate in your dataframe to use this function.")
    
    # check for other variables
    for var in ['year','month','day','time']:
        if var in dataframe.columns:
            dtypes = dataframe[var].dtypes
            if type(dtypes) is np.dtypes.ObjectDType:
                print("figure something out")
            elif var != 'time' and type(dtypes) is not int:
                raise ValueError("{} is not the correct type.  It should be int".format(var))
            elif var == 'time' and type(dtypes) is not isinstance(dtypes,datetime.date):
                raise ValueError("Time should be converted to a datetime object.")
            else:
                raise ValueError("check the dtypes: {}".format(dtypes))