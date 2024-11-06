def check_occurrenceIDs(dataframe=None):
    """
    Checks whether or not you have unique ids for your occurrences.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """
    list_terms = list(dataframe.columns)
    unique_id_columns = ['occurrenceID','catalogNumber','recordNumber']
    for id in unique_id_columns:
        if id in list_terms:
            if len(list(set(dataframe[id]))) < len(list(dataframe[id])):
                raise ValueError("There are duplicate {}s".format(id)) 