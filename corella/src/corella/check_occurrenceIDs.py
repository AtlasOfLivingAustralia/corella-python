def check_occurrenceIDs(dataframe=None,
                        errors=[]):
    """
    Checks whether or not you have unique ids for your occurrences.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    # First, check if a dataframe is provided
    if dataframe is None:
        raise ValueError("Please provide a dataframe to this function.")

    # look for duplicate unique IDs
    list_terms = list(dataframe.columns)
    unique_id_columns = ['occurrenceID','catalogNumber','recordNumber']
    for id in unique_id_columns:
        if id in list_terms:
            if len(list(set(dataframe[id]))) < len(list(dataframe[id])):
                errors.append("There are duplicate {}s".format(id)) 

    # return any errors found
    return errors