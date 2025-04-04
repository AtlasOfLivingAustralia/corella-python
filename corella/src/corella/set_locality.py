from .check_locality import check_locality
from .common_functions import check_for_dataframe,set_data_workflow

def set_locality(dataframe=None,
                 continent = None,
                 country = None,
                 countryCode = None,
                 stateProvince = None,
                 locality = None):
    """
    Checks for additional location information, such as country and countryCode.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        continent: ``str``
            Either a column name (``str``) or a string denoting one of the seven continents.
        country: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a string denoting the country.
        countryCode: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a string denoting the countryCode.
        stateProvince: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a string denoting the state or province.
        locality: ``str`` or ``pandas.Series``
            Either a column name (``str``) or a string denoting the locality.
    Returns
    -------
        ``pandas.DataFrame`` with the updated data.
    """

    # check for dataframe
    check_for_dataframe(dataframe=dataframe,func='set_locality')

    # create a dictionary of names for renaming
    mapping = {
        'continent': continent,
        'country': country,
        'countryCode': countryCode,
        'stateProvince': stateProvince,
        'locality': locality
    }

    accepted_formats = {
        'continent': [str],
        'country': [str],
        'countryCode': [str],
        'stateProvince': [str],
        'locality': [str]
    }

    # specify values
    variables = [continent,country,countryCode,stateProvince,locality]
    values = ['continent','country','countryCode','stateProvince','locality']

    dataframe = set_data_workflow(func='set_locality',dataframe=dataframe,mapping=mapping,variables=variables,
                                  values=values,accepted_formats=accepted_formats)
    
    # get errors in data
    errors = check_locality(dataframe=dataframe)

    # return errors if there are any; otherwise, 
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe