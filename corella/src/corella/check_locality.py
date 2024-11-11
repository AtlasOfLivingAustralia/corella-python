import os
import pandas as pd
from .common_dictionaries import continents
from .common_functions import check_is_string

def check_locality(dataframe=None,
                   errors=[]):
    """
    Checks whether or not your locality data complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.
    """
    # get country codes for checking
    country_codes = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wikipedia_country_codes.csv'))

    # column names for easy looping
    column_names = {
        'country': 'Country name',
        'countryCodes': 'Code'
    }

    # loop over all variables
    for var in ['continent','country','countryCode','stateProvince','locality']:
        if var in dataframe.columns:
            errors = check_is_string(dataframe=dataframe,column_name=var,errors=errors)
            if var == 'continent':
                if not set(continents).issuperset(dataframe[var]):
                    errors.append('Some of your continents are incorrect.  Accepted values are:\n\n{}'.format(', '.join(continents)))
            elif var == 'country' or var == 'countryCode':
                if not set(country_codes[column_names[var]]).issuperset(dataframe[var]):
                    errors.append('Some of your {} are incorrect.  Accepted values are found on Wikipedia: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'.format(var))
            
    # return errors
    if errors is not None:
        return errors
    return None