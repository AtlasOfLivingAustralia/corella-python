from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_string_dtype
from .common_dictionaries import GEO_REQUIRED_DWCA_TERMS

def check_coordinates(dataframe=None):
    """
    Checks whether or not your occurrences data complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        If something is not valid, raises a ``ValueError``.
        Else, returns None.
    """

    # check data types for location data
    for c in GEO_REQUIRED_DWCA_TERMS["Australia"]:
        if c in dataframe.columns:
            data_type = dataframe[c].dtypes
            
            if c in ['decimalLatitude','decimalLongitude','coordinatePrecision'] and not is_numeric_dtype(dataframe[c]):
                raise ValueError("Column {} needs to be of type float.  Currently, it is {}.".format(c,data_type))
            else:
                pass

            if c == 'coordinateUncertaintyInMeters' and not is_numeric_dtype(dataframe[c]):
                raise ValueError("Column {} needs to be of type float or type int.  Currently, it is {}.".format(c,data_type))
            else:
                pass

            if c == 'geodeticDatum' and not is_string_dtype(dataframe[c]):
                raise ValueError("Column {} needs to be of type str.  Currently, it is {}.".format(c,data_type))
            else:
                pass
        # elif c in ['geodeticDatum','coordinateUncertaintyInMeters','coordinatePrecision']:
        #     print('We noticed that you have not provided a {}.  We will then assume the default is {}.'.format(c,defaults[c]))
                
    # check range of lat/long are correct
    lat_valid_count = dataframe['decimalLatitude'].astype(float).between(-90, 90, inclusive='both').sum()
    lon_valid_count = dataframe['decimalLongitude'].astype(float).between(-180, 180, inclusive='both').sum()

    if lat_valid_count < len(dataframe['decimalLatitude']):
        raise ValueError("There are some invalid latitude values.  They should be between -90 and 90.")

    if lon_valid_count < len(dataframe['decimalLongitude']):
        raise ValueError("There are some invalid longitude values.  They should be between -180 and 180.")
