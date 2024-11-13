import pandas as pd
from .add_unique_occurrence_ids import add_unique_occurrence_IDs
from .check_occurrences import check_occurrences

def use_occurrences(dataframe=None,
                    occurrenceID=None,
                    catalogNumber=None,
                    recordNumber=None,
                    basisOfRecord=None,
                    occurrenceStatus=None,
                    errors=[]):
    """
    Checks for unique identifiers of each occurrence and how the occurrence was recorded.

    Parameters
    ----------
        occurrenceID: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the unique occurrenceIDs of the occurrences.
        basisOfRecord: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents how the occurrence was recorded.

    Returns
    -------
        Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
    """

    # First, check if a dataframe is provided
    if dataframe is None:
        raise ValueError("Please provide a dataframe to this function.")

    # column renaming dictionary
    renaming_map = {
        occurrenceID: 'occurrenceID',
        catalogNumber: 'catalogNumber',
        recordNumber: 'recordNumber',
        basisOfRecord: 'basisOfRecord',
        occurrenceStatus: 'occurrenceStatus'
    }

    # loop over all possible arguments
    if any(x is not None for x in [renaming_map.keys()]):

        for var in renaming_map.keys():

            if var is not None:
                if (type(var) is bool) and (var in [occurrenceID,catalogNumber,recordNumber]) and (renaming_map[var] not in dataframe.columns):
                    dataframe = add_unique_occurrence_IDs(column_name=renaming_map[var],dataframe=dataframe)
                elif type(var) is str:
                    if var in dataframe.columns and var is not basisOfRecord:
                        index = list(dataframe.columns).index(var)
                        dataframe = dataframe.rename(columns={dataframe.columns[index]: renaming_map[var]})
                    else:
                        dataframe[renaming_map[var]] = basisOfRecord
                else:
                    raise ValueError("occurrenceID argument must be a string or a boolean.")

    else:
        
        raise ValueError("No Darwin Core arguments supplied to `use_occurrences()`.  See dir(corella.use_occurrences()) for valid arguments.")
        
    # check data
    errors = check_occurrences(dataframe=dataframe,errors=[])

    # return errors if there are any; otherwise, 
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe