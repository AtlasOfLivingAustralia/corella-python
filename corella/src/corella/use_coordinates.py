import pandas as pd
from .check_coordinates import check_coordinates

def use_coordinates(dataframe=None,
                    decimalLatitude=None,
                    decimalLongitude=None,
                    geodeticDatum=None,
                    coordinateUncertaintyInMeters=None,
                    coordinatePrecision=None):
    """
    Checks for location information, as well as uncertainty and coordinate reference system.  
    Also runs data checks on coordinate validity.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        decimalLatitude: ``str``
            A column name (``str``) that contains your latitudes (units in degrees).
        decimalLongitude: ``str`` or ``pandas.Series``
            A column name (``str``) that contains your longitudes (units in degrees).
        geodeticDatum: ``str`` 
            A column name (``str``) or a ``str`` with the name of a valid Coordinate 
            Reference System (CRS).
        coordinateUncertaintyInMeters: ``str``, ``float`` or ``int`` 
            A column name (``str``) or a ``str`` with the name of a valid Coordinate 
            Reference System (CRS).
        coordinatePrecision: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the inherent uncertainty of your measurement 
            (unit in degrees).

    Returns
    -------
        ``pandas.DataFrame`` with the updated data.
    """

    # mapping column names
    mapping = {
        decimalLatitude: 'decimalLatitude',
        decimalLongitude: 'decimalLongitude', 
        geodeticDatum: 'geodeticDatum',
        coordinatePrecision: 'coordinatePrecision',
        coordinateUncertaintyInMeters: 'coordinateUncertaintyInMeters'
    }

    # accepted formats for inputs
    accepted_formats = {
        decimalLatitude: [float],
        decimalLongitude: [float], 
        geodeticDatum: [str],
        coordinatePrecision: [float],
        coordinateUncertaintyInMeters: [float,int]
    }

    # check if each variable is None
    if all([v is None for v in [decimalLatitude,decimalLongitude,geodeticDatum,coordinatePrecision,coordinateUncertaintyInMeters]]):
        raise ValueError("No Darwin Core arguments supplied to `use_occurrences()`.  See dir(self.use_coordinates()) for valid arguments.")

    # loop over all variables with following logic:
    # 1. check if var is None
    # 2.   If var is not none, and not in the column names, assume user has given us a value for the column and add it; 
    #        delete entry in dictionary, as column does not need to be renamed 
    for var in [decimalLatitude,decimalLongitude,geodeticDatum,coordinatePrecision,coordinateUncertaintyInMeters]:
        if var is not None:
            if var not in dataframe.columns:
                if type(var) in accepted_formats[var]:
                    dataframe[mapping[var]] = var
                    del mapping[var]
                else:
                    raise ValueError("Only a {} is accepted for {}".format(accepted_formats[var],var))

    # rename all necessary columns
    dataframe = dataframe.rename(columns=mapping)

    # check all required variables
    check_coordinates(dataframe=dataframe)

    # set new occurrences to object
    return dataframe