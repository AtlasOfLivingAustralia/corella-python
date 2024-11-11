from .get_dwc_noncompliant_terms import get_dwc_noncompliant_terms
from .check_abundance import check_abundance
from .check_basisOfRecord import check_basisOfRecord
from .check_coordinates import check_coordinates
from .check_datetime import check_datetime
from .check_locality import check_locality
from .check_occurrenceIDs import check_occurrenceIDs
from .check_scientificName import check_scientificName

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

        # initialise errors 
        errors = []

        # first, check for all terms that are not compliant
        vocab_check = get_dwc_noncompliant_terms(dataframe = dataframe)
        if len(vocab_check) > 0:
            errors.append("Your column names do not comply with the DwC standard.")
        
        # run all checks
        errors = check_abundance(dataframe=dataframe,errors=errors)
        errors = check_basisOfRecord(dataframe=dataframe,errors=errors)
        errors = check_coordinates(dataframe=dataframe,errors=errors)
        errors = check_datetime(dataframe=dataframe,errors=errors)
        errors = check_locality(dataframe=dataframe,errors=errors)
        errors = check_occurrenceIDs(dataframe=dataframe,errors=errors)
        errors = check_scientificName(dataframe=dataframe,errors=errors)

        # print out message to screen
