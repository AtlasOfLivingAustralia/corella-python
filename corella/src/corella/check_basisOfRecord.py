import pandas as pd
from .common_functions import snake_to_camel_case

def check_basisOfRecord(dataframe=None):
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
        bor_column = list(dataframe["basisOfRecord"])
        types_bor = list(set(list(type(x) for x in bor_column)))
        if len(types_bor) > 1:
            raise ValueError("There are multiple types in the basisOfRecord column - ensure that there are only strings")
        else:
            if types_bor[0] is not str:
                raise ValueError("basisOfRecord column should only contain strings")
            else:
                temp = pd.read_table('https://raw.githubusercontent.com/gbif/parsers/dev/src/main/resources/dictionaries/parse/basisOfRecord.tsv').dropna()
                terms = list(set(temp['PRESERVED_SPECIMEN']))
                terms = snake_to_camel_case(terms)
                if not set(terms).issuperset(set(dataframe['basisOfRecord'])):
                    raise ValueError("There are invalid basisOfRecord values.  Valid values are {}".format(', '.join(terms)))
    else:
        raise ValueError("The basisOfRecord column title wasn't set correctly.")