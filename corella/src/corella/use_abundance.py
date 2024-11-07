def use_abundance(dataframe=None,
                  individualCount=None,
                  organismQuantity=None,
                  organismQuantityType=None):
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

    Returns
    -------
        Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
    """

    if dataframe is None:
        raise ValueError('Please provide a dataframe to use_abundance().')
    
    # for column in [individualCount,organismQuantity,organismQuantityType]:
