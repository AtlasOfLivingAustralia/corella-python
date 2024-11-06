def check_locality(dataframe=None):
    """
    Checks whether or not your locality data complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.
    """

    continents = ["Africa","Antarctica","Asia","Europe","North America","Oceania","South America"]
    
    for var in ['continent','country','countryCode','stateProvince','locality']:
        if var in dataframe.columns:
            loc_column = list(dataframe[var])
            types_loc = list(set(list(type(x) for x in loc_column)))
            if len(types_loc) > 1:
                raise ValueError("There are multiple types in the eventDate column - ensure that there are only datetime objects")
            else:
                if not isinstance(types_loc[0], str):
                    raise ValueError("Data needs to be in string format.")
                else:
                    if var == 'continent':
                        if not set(continents).issuperset(set(dataframe[var])):
                            raise ValueError("Some of your continent values are incorrect.")