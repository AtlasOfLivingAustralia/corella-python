from .common_functions import check_is_string

def check_scientificName(dataframe=None,
                         errors=[]):
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
    # first, check if a dataframe has been provided
    if dataframe is None:
        raise ValueError("You need to provide a dataframe")

    # then, check to see for the required columns
    if 'scientificName' not in dataframe.columns:
        errors.append('scientificName is a required column.')

    # check the type of variable for all scientific name associated variables
    for item in ['scientificName','scientificNameRank','scientificNameAuthorship']:
        if item in dataframe.columns:
            errors = check_is_string(dataframe=dataframe,column_name=item,errors=errors)

    # return either errors or None
    if errors is not None:
        return errors
    return None