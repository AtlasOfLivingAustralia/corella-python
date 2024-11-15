from .check_scientificName import check_scientificName

def use_scientific_name(dataframe=None,
                        scientificName=None):
    """
    Checks for the name of the taxon you identified is present.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        scientificName: ``str``
            A column name (``str``) denoting all your scientific names.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data.
    """

    # check for dataframe
    if dataframe is None:
        raise ValueError('Please provide a dataframe.')

    # check for validating data
    if scientificName is None:
        if 'scientificName' not in dataframe.columns:
            raise ValueError("No Darwin Core arguments supplied to `use_scientific_name()`.  See dir(corella.use_scientific_name()) for valid arguments.")

    # now, do the checking
    elif scientificName is not None:

        # check type of variable
        if type(scientificName) is str:
            if scientificName in dataframe.columns:
                dataframe = dataframe.rename(columns={scientificName: 'scientificName'})
        else:
            raise ValueError("scientificName argument must be a string (column name).")

    # check values
    errors = check_scientificName(dataframe=dataframe)
                    
    # return errors if there are any; otherwise, 
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe 