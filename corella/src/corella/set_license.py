from .check_license import check_license
from .common_functions import check_for_dataframe,set_data_workflow

def set_license(dataframe=None,
                license=None,
                rightsHolder=None,
                accessRights=None):
    """
    Checks for location information, as well as uncertainty and coordinate reference system.  
    Also runs data checks on coordinate validity.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check
        license: ``str``
            A column name (``str``) that contains your individual counts (should be whole numbers).
        rightsHolder: ``str`` or 
            A column name (``str``) that contains a description of your individual counts.
        accessRights: ``str`` 
            A column name (``str``) that describes what your rightsHolder is.

    Returns
    -------
        ``pandas.DataFrame`` with the updated data.
    """

    # raise a ValueError if no dataframe is provided
    check_for_dataframe(dataframe=dataframe,func='set_license')
    
    # column renaming dictionary
    mapping = {
        'license': license ,
        'rightsHolder': rightsHolder,
        'accessRights': accessRights,
    }

    # denote accepted formats
    accepted_formats = {
        'license': [str,list],
        'rightsHolder': [str,list],
        'accessRights': [str,list],
    }

    # manually set values for function
    variables = [license,rightsHolder,accessRights]
    values = ['license','rightsHolder','accessRights']

    # set all values in dataframe
    dataframe = set_data_workflow(func='set_license',dataframe=dataframe,mapping=mapping,variables=variables,
                                  values=values,accepted_formats=accepted_formats)

    # check errors in data
    errors = check_license(dataframe=dataframe,errors=[])
    
    # return errors if there are any; otherwise, return dataframe
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe