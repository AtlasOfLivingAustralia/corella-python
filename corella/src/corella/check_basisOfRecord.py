from .common_functions import get_bor_values,check_is_string

def check_basisOfRecord(dataframe=None,
                        errors=[]):
    """
    Checks whether or not your basisOfRecord values are valid.

    Parameters
    ----------
        None

    Returns
    -------
        If one of your entries is not valid, raises a ``ValueError`` with a list of accepted terms.
        Else, returns None
    """

    # check if dataframe is provided an argument
    if dataframe is None:
        raise ValueError("You need to provide a dataframe")

    # check basisOfRecord values
    if 'basisOfRecord' in dataframe.columns:
        errors = check_is_string(dataframe=dataframe,column_name='basisOfRecord',errors=errors)
        terms = get_bor_values()
        if not set(terms).issuperset(set(dataframe['basisOfRecord'])):
            errors.append("There are invalid basisOfRecord values.  Valid values are {}".format(', '.join(terms)))
    else:
        errors.append("The basisOfRecord column title wasn't set correctly.")

    # return errors or None if no errors
    if errors is not None:
        return errors
    return None