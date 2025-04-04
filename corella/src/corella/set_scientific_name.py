from .check_scientificName import check_scientificName
from .common_functions import check_for_dataframe,set_data_workflow

def set_scientific_name(dataframe=None,
                        scientificName=None,
                        taxonRank=None,
                        scientificNameAuthorship=None):
    """
    Checks for the name of the taxon you identified is present.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        scientificName: ``str``
            A column name (``str``) denoting all your scientific names.
        taxonRank: ``str``
            A column name (``str``) denoting the rank of your scientific names (species, genus etc.)
        scientificNameAuthorship: ``str``
            A column name (``str``) denoting who originated the scientific name.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data.
    """

    # check for dataframe
    check_for_dataframe(dataframe=dataframe,func='set_scientific_name')
    
    mapping = {
        'scientificName': scientificName,
        'taxonRank': taxonRank,
        'scientificNameAuthorship': scientificNameAuthorship
    }

    accepted_formats = {
        'scientificName': [str],
        'taxonRank': [str],
        'scientificNameAuthorship': [str]
    }

    variables = [scientificName,taxonRank,scientificNameAuthorship]
    values = ['scientificName','taxonRank','scientificNameAuthorship']

    dataframe = set_data_workflow(func='set_taxonomy',dataframe=dataframe,mapping=mapping,variables=variables,
                                  values=values,accepted_formats=accepted_formats)

    # check values
    errors = check_scientificName(dataframe=dataframe)
                    
    # return errors if there are any; otherwise, 
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe 