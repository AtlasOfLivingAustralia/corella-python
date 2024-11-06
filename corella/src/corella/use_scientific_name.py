def use_scientific_name(self,scientific_name=None):
    """
    Checks for the name of the taxon you identified is present.

    Parameters
    ----------
        scientific_name: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a column from the ``occurrences`` argument 
            (``pandas.Series``) that represents the taxonomic identification of the occurrences.

    Returns
    -------
        Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
    """

    if scientific_name is not None:

        # create temporary occurrences
        temp_occurrences = self.occurrences.copy()

        # check type of variable
        if type(scientific_name) is pd.core.series.Series:
            temp_occurrences['scientificName'] = scientific_name.copy()
            temp_occurrences = temp_occurrences.drop(scientific_name.name,axis=1)
        else:
            raise ValueError("scientific_name argument must be a pandas Series (i.e. column)")

        # check values
        check_scientificName(dataframe=temp_occurrences)

        # assign temp_occurrences to occurrences
        self.occurrences = temp_occurrences
    
    else:

        raise ValueError("No Darwin Core arguments supplied to `use_scientific_name()`.  See dir(self.use_scientific_name()) for valid arguments.")