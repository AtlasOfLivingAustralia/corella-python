def use_locality(self,
                    continent = None,
                    country = None,
                    countryCode = None,
                    stateProvince = None,
                    locality = None):
    """
    (OPTIONAL) Checks for additional location information, such as country and countryCode.

    Parameters
    ----------
        continent: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the continent of the occurrences.
        country: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the country of the occurrence.
        countryCode: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the countryCode of the occurrences.
        stateProvince: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the stateProvince of the occurrences.
        locality: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the locality of the occurrences.
    Returns
    -------
        Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
    """

    if all(map(lambda v: v not in ["continent","country","countryCode","stateProvince", "locality"],list(self.occurrences.columns))):
        raise ValueError("No Darwin Core arguments supplied to `use_locality()`.  See dir(self.use_locality()) for valid arguments.")
    
    # create a temporary occurrences variable
    temp_occurrences = self.occurrences

    # create a dictionary of names for renaming
    names = {}

    for var in [continent,country,countryCode,stateProvince,locality]:
        if var is not None and var is continent:
            names[var.name] = 'continent'
        elif var is not None and var is country:
            names[var.name] = 'country'
        elif var is not None and var is countryCode:
            names[var.name] = 'countryCode'
        elif var is not None and var is stateProvince:
            names[var.name] = 'stateProvince'
        elif var is not None and var is locality:
            names[var.name] = 'locality'
        else:
            pass

    # check name of columns
    for var in [continent,country,countryCode,stateProvince,locality]:
        if var is not None:        
            if type(var) is str:
                pass
            elif type(var) is pd.core.series.Series:
                temp_occurrences = temp_occurrences.rename(columns={var.name: names[var.name]})
            else:
                raise ValueError("only accepts str types or pandas series as {}".format(var.name))
    
    check_locality(dataframe=temp_occurrences)

    self.occurrences = temp_occurrences