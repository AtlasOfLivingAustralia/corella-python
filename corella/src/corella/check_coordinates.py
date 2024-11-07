from pandas.api.types import is_numeric_dtype,is_string_dtype
from .common_dictionaries import GEO_REQUIRED_DWCA_TERMS

def check_coordinates(dataframe=None):
    """
    Checks whether or not your occurrences data complies with 
    Darwin Core standards.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check.

    Returns
    -------
        Raises a ``ValueError``, else, return None.
    """
    # First, check if a dataframe is provided
    if dataframe is None:
        raise ValueError("Please provide a dataframe to this function.")

    # make a list of errors to return
    errors = []

    # check data types for location data
    for c in GEO_REQUIRED_DWCA_TERMS["Australia"]:
        if c in dataframe.columns:
            data_type = dataframe[c].dtypes
            
            if c in ['decimalLatitude','decimalLongitude','coordinatePrecision'] and not is_numeric_dtype(dataframe[c]):
                errors.append("Column {} needs to be of type float.  Currently, it is {}.".format(c,data_type))
            else:
                pass

            if c == 'coordinateUncertaintyInMeters' and not is_numeric_dtype(dataframe[c]):
                errors.append("Column {} needs to be of type float or type int.  Currently, it is {}.".format(c,data_type))
            else:
                pass

            if c == 'geodeticDatum' and not is_string_dtype(dataframe[c]):
                errors.append("Column {} needs to be of type str.  Currently, it is {}.".format(c,data_type))
            else:
                pass
                
    # set ranges for easy looping
    ranges = {
        'decimalLatitude': [-90,90],
        'decimalLongitude': [-180,180]
    }

    # check range of lat/long are correct
    for var in ['decimalLatitude','decimalLongitude']:

        # check for any entries that aren't valid
        if var in dataframe.columns:

            valid_count = dataframe[var].astype(float).between(ranges[var][0], ranges[var][1], inclusive='both').sum()

            # return errors
            if valid_count < len(dataframe[var]):
                errors.append("There are some invalid {} values.  They should be between {} and {}.".format(var,ranges[var][0],ranges[var][1]))

    # make sure that any uncertainty provided is above 0
    for var in ['coordinateUncertaintyInMeters','coordinatePrecision']:
    
        if var in dataframe.columns and is_numeric_dtype(dataframe[var]):

            valid_count_df = dataframe[var] > 0
            valid_count = valid_count_df.sum()

            # return errors
            if valid_count < len(dataframe[var]):
                errors.append("There are some invalid {} values.  They should be above 0.".format(var))
          
    # return both errors 
    if errors is not None:
        return errors
    return None
