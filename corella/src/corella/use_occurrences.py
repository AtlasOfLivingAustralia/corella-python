def use_occurrences(self,occurrenceID=None,basisOfRecord=None):
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

    if occurrenceID is not None or basisOfRecord is not None:

        # create temporary occurrences
        temp_occurrences = self.occurrences.copy()

        if occurrenceID is not None:
            if type(occurrenceID) is bool:
                temp_occurrences = add_unique_occurrence_IDs(column_name='occurrenceID',
                                                                dataframe=temp_occurrences)
            elif type(occurrenceID) is pd.core.series.Series:
                temp_occurrences['occurrenceID'] = occurrenceID.copy()
                temp_occurrences.drop(occurrenceID.name,axis=1)
            else:
                raise ValueError("occurrenceID argument must be a boolean or pandas Series (i.e. column)")

            # check values
            check_occurrenceIDs(dataframe=temp_occurrences)

        if basisOfRecord is not None:
            if type(basisOfRecord) is str:
                temp_occurrences['basisOfRecord'] = basisOfRecord
            elif type(basisOfRecord) is pd.core.series.Series:
                temp_occurrences['basisOfRecord'] = basisOfRecord.copy()
                temp_occurrences.drop(basisOfRecord.name,axis=1)
            else:
                raise ValueError("occurrenceID argument must be a string or pandas Series (i.e. column)")

            # check values
            check_basisOfRecord(dataframe=temp_occurrences) 

    else:
        
        raise ValueError("No Darwin Core arguments supplied to `use_occurrences()`.  See dir(self.use_occurrences()) for valid arguments.")
        

    # assign new occurrences to archive
    self.occurrences = temp_occurrences