from .check_locality import check_locality

def use_locality(dataframe=None,
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

    # check for dataframe
    if dataframe is None:
        raise ValueError('Please provide a dataframe.')

    # check for validating data
    if all([v is None for v in [continent,country,countryCode,stateProvince,locality]]):
        if all ([v not in ['continent','country','countryCode','stateProvince','locality'] for v in dataframe.columns]):
            raise ValueError("No Darwin Core arguments supplied to `use_locality()`.  See dir(self.use_locality()) for valid arguments.")

    # create a dictionary of names for renaming
    names = {
        continent: 'continent',
        country: 'country',
        countryCode: 'countryCode',
        stateProvince: 'stateProvince',
        locality: 'locality'
    }

    # check name of columns
    for var in [continent,country,countryCode,stateProvince,locality]:
        if var is not None:        
            if type(var) is str:
                if var in dataframe.columns:
                    dataframe = dataframe.rename(columns={var: names[var]})
                else:
                    if not dataframe.empty:
                        dataframe[names[var]] = var
                    else:
                        raise ValueError('This is an empty dataframe')
            else:
                raise ValueError("only accepts str types".format(var.name))
    
    # get errors in data
    errors = check_locality(dataframe=dataframe)

    # return errors if there are any; otherwise, 
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe