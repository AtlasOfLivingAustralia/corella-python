from .check_abundance import check_abundance
from .check_basisOfRecord import check_basisOfRecord
from .check_occurrenceIDs import check_occurrenceIDs

def check_occurrences(dataframe=None,
                      errors=[]):
    """
    Comments here later.
    """

    errors = check_basisOfRecord(dataframe=dataframe,errors=errors)
    errors = check_occurrenceIDs(dataframe=dataframe,errors=errors)
    errors = check_abundance(dataframe=dataframe,errors=errors)

    return errors