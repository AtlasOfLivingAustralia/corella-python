from .get_dwc_noncompliant_terms import get_dwc_noncompliant_terms
from .check_occurrenceIDs import check_occurrenceIDs

def check_occurrences(dataframe=None):
        """
        Checks whether or not your occurrences data complies with 
        Darwin Core standards.

        Parameters
        ----------
            None

        Returns
        -------
            Raises a ``ValueError`` if something is not valid.
        """

        # run basic checks
        vocab_check = get_dwc_noncompliant_terms(dataframe = dataframe)
        if len(vocab_check) > 0:
            raise ValueError("Your column names do not comply with the DwC standard.")
        
        # # TODO: check all values in vocab are there
        # values_check = check_dwca_values(dataframe=dataframe)
        # if type(values_check) is not bool:
        #     raise ValueError("The values in some of your columns do not comply with the DwC standard.")
        
        # check for presence of occurrenceID
        if 'occurrenceID' not in list(dataframe):
            raise ValueError("You need to add unique identifiers into your occurrences.")
        
        # check for unique ids
        unique_id_check = check_occurrenceIDs(dataframe=dataframe)
        if not unique_id_check:
            list_event_ids = list(dataframe['occurrenceID'])
            duplicates = [x for x in list_event_ids if list_event_ids.count(x) >= 2]
            raise ValueError("There are some duplicate eventIDs: {}".format(duplicates))
        
        return True