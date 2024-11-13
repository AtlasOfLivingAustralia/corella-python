from .check_abundance import check_abundance

def use_abundance(dataframe=None,
                  individualCount=None,
                  organismQuantity=None,
                  organismQuantityType=None):
    """
    Checks for location information, as well as uncertainty and coordinate reference system.  
    Also runs data checks on coordinate validity.

    Parameters
    ----------
        X

    Returns
    -------
        Raises a ``ValueError`` explaining what is wrong, or returns None if it passes.
    """

    # raise a ValueError if no dataframe is provided
    if dataframe is None:
        raise ValueError('Please provide a dataframe.')
    
    # column renaming dictionary
    renaming_map = {
        individualCount: 'individualCount',
        organismQuantity: 'organismQuantity',
        organismQuantityType: 'organismQuantityType',
    }

    # loop over all possible arguments
    if any(x is not None for x in [renaming_map.keys()]):

        for var in renaming_map.keys():

            if var is not None:
                if type(var) is str:
                    if var in dataframe.columns:
                        index = list(dataframe.columns).index(var)
                        dataframe = dataframe.rename(columns={dataframe.columns[index]: renaming_map[var]})
                else:
                    raise ValueError("{} argument must be a string.".format(renaming_map[var]))

    # check errors in data
    errors = check_abundance(dataframe=dataframe,errors=[])
    
    # return errors if there are any; otherwise, return dataframe
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe