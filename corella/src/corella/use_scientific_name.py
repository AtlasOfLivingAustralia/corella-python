from .check_scientificName import check_scientificName

def use_scientific_name(dataframe=None,
                        scientificName=None):
    """
    Checks for the name of the taxon you identified is present.

    Parameters
    ----------
        scientificName: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the taxonomic identification of the occurrences.

    Returns
    -------
        Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
    """

    if scientificName is not None:

        # check type of variable
        if type(scientificName) is str:
            if scientificName in dataframe.columns:
                dataframe = dataframe.rename(columns={scientificName: 'scientificName'})
        else:
            raise ValueError("scientificName argument must be a pandas Series (i.e. column)")

        # check values
        errors = check_scientificName(dataframe=dataframe)
        return errors       
    
    else:

        raise ValueError("No Darwin Core arguments supplied to `use_scientific_name()`.  See dir(self.use_scientific_name()) for valid arguments.")