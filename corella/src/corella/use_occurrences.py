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
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        occurrenceID: ``str`` or ``bool``
            Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
            provided, the column will be renamed.  If ``True`` is provided, unique identifiers
            will be generated in the dataset.
        catalogNumber: ``str`` or ``bool``
            Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
            provided, the column will be renamed.  If ``True`` is provided, unique identifiers
            will be generated in the dataset.
        recordNumber: ``str`` or ``bool``
            Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
            provided, the column will be renamed.  If ``True`` is provided, unique identifiers
            will be generated in the dataset.
        basisOfRecord: ``str``
            Either a column name (``str``) or a valid value for ``basisOfRecord`` to add to 
            the dataset.
        occurrenceStatus: ``str``
            Either a column name (``str``) or a valid value for ``occurrenceStatus`` to add to 
            the dataset.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data.
    """

    # check for dataframe
    if dataframe is None:
        raise ValueError('Please provide a dataframe.')

    # check for validating data
    if all([v is None for v in [occurrenceID,catalogNumber,recordNumber,basisOfRecord,occurrenceStatus]]):
        if all ([v not in ['occurrenceID','catalogNumber','recordNumber','basisOfRecord','occurrenceStatus'] for v in dataframe.columns]):
            raise ValueError("No Darwin Core arguments supplied to `use_occurrences()`.  See dir(corella.use_occurrences()) for valid arguments.")

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
                    if var in dataframe.columns: 
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