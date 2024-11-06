def check_scientificName(dataframe=None):
    """
    Checks whether or not the following columns are in string format:

    - scientificName
    - scientificNameRank
    - scientificNameAuthorship

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    if dataframe is None:
        raise ValueError("You need to provide a dataframe")

    for item in ['scientificName','scientificNameRank','scientificNameAuthorship']:
        if item in dataframe.columns:
            sn_column = list(dataframe[item])
            types_data = list(set(list(type(x) for x in sn_column)))
            if len(types_data) > 1:
                raise ValueError("There are multiple types in the {} column - ensure that there are only strings".format(item))
            else:
                if types_data[0] is not str:
                    raise ValueError("{} column should only contain strings".format(item))
        elif item == 'scientificName': 
            raise ValueError("The scientificName column title wasn't set correctly.")