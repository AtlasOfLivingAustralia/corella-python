from .check_coordinates import check_coordinates

def use_coordinates(dataframe=None,
                    decimalLatitude=None,
                    decimalLongitude=None,
                    geodeticDatum=None,
                    coordinateUncertaintyInMeters=None,
                    coordinatePrecision=None,
                    assign = True):
    """
    Checks for location information, as well as uncertainty and coordinate reference system.  
    Also runs data checks on coordinate validity.

    Parameters
    ----------
        decimalLatitude: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents latitude (unit in degrees).
        decimalLongitude: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents longitude (unit in degrees).
        geodeticDatum: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the coordinate reference system (CRS).
        coordinateUncertaintyInMeters: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the uncertainty of the instrument measuring 
            the latitude and longitude (unit is meters).
        coordinatePrecision: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the inherent uncertainty of your measurement 
            (unit in degrees).

    Returns
    -------
        Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
    """

    # make copy of occurrences
    temp_occurrences = self.occurrences.copy()

    # mapping here for later
    mapping = {}

    if all([v is None for v in [decimalLatitude,decimalLongitude,geodeticDatum,coordinatePrecision,coordinateUncertaintyInMeters]]):
        raise ValueError("No Darwin Core arguments supplied to `use_occurrences()`.  See dir(self.use_coordinates()) for valid arguments.")

    # check if each variable is None
    if decimalLatitude is not None:
        mapping[decimalLatitude.name] = 'decimalLatitude'

    if decimalLongitude is not None:
        mapping[decimalLongitude.name] = 'decimalLongitude'

    if geodeticDatum is not None:
        if type(geodeticDatum) is pd.core.series.Series:
            mapping[geodeticDatum.name] = 'geodeticDatum'
        elif type(geodeticDatum) is str:
            temp_occurrences['geodeticDatum'] = geodeticDatum
        else:
            raise ValueError("Only a string or pandas series is accepted for geodeticDatum")

    if coordinateUncertaintyInMeters is not None:
        if type(coordinateUncertaintyInMeters) is pd.core.series.Series:
            mapping[coordinateUncertaintyInMeters.name] = 'coordinateUncertaintyInMeters'
        elif (type(coordinateUncertaintyInMeters) is int or type(coordinateUncertaintyInMeters) is float):
            temp_occurrences['coordinateUncertaintyInMeters'] = coordinateUncertaintyInMeters
        else:
            raise ValueError("Only an int, float or pandas series is accepted for coordinateUncertaintyInMeters")

    if coordinatePrecision is not None:
        if type(coordinatePrecision) is pd.core.series.Series:
            mapping[coordinatePrecision.name] = 'coordinatePrecision'
        elif (type(coordinatePrecision) is int or type(coordinatePrecision) is float):
            temp_occurrences['coordinatePrecision'] = coordinatePrecision
        else:
            raise ValueError("Only an int, float or pandas series is accepted for coordinatePrecision")

    # rename all necessary columns
    temp_occurrences = temp_occurrences.rename(columns=mapping)

    # check all required variables
    check_coordinates(dataframe=temp_occurrences)

    # set new occurrences to object
    if assign:
        self.occurrences = temp_occurrences
    else:
        print(temp_occurrences)