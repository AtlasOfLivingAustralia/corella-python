from .common_dictionaries import GEO_REQUIRED_DWCA_TERMS
from .check_coordinates import check_coordinates
from .common_functions import check_for_dataframe,set_data_workflow

def set_coordinates(dataframe=None,
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
            A column name (``str``) or a ``float``/``int`` with the name of a valid Coordinate 
            Reference System (CRS).
        coordinatePrecision: ``str``, ``float`` or ``int``
            Either a column name (``str``) or a ``float``/``int`` that represents the inherent 
            uncertainty of your measurement (unit in degrees).

    Returns
    -------
        ``pandas.DataFrame`` with the updated data.
    """

    # raise a ValueError if no dataframe is provided
    check_for_dataframe(dataframe=dataframe,func='set_coordinates')

    # mapping column names
    mapping = {
        'decimalLatitude': decimalLatitude,
        'decimalLongitude': decimalLongitude, 
        'geodeticDatum': geodeticDatum,
        'coordinatePrecision': coordinatePrecision,
        'coordinateUncertaintyInMeters': coordinateUncertaintyInMeters
    }

    # accepted formats for inputs
    accepted_formats = {
        'decimalLatitude': [float],
        'decimalLongitude': [float], 
        'geodeticDatum': [str],
        'coordinatePrecision': [float,int],
        'coordinateUncertaintyInMeters': [float,int]
    }

    variables = [decimalLatitude,decimalLongitude,geodeticDatum,coordinatePrecision,coordinateUncertaintyInMeters]
    values = ['decimalLatitude','decimalLongitude','geodeticDatum','coordinatePrecision','coordinateUncertaintyInMeters']

    dataframe = set_data_workflow(func='set_coordinates',dataframe=dataframe,mapping=mapping,variables=variables,
                                  values=values,accepted_formats=accepted_formats)

    # check all required variables
    errors = check_coordinates(dataframe=dataframe,errors=[])

    # return errors if there are any; otherwise, return dataframe
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe