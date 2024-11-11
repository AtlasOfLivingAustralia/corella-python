from .common_dictionaries import unique_messages
from .common_functions import check_is_numeric,check_is_string,swap_error_message

def check_abundance(dataframe=None,
                    errors=[]):
    """
    Checks whether or not your abundance data...

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check.

    Returns
    -------
        A list of errors; else, return None.
    """

    # check if dataframe is provided an argument
    if dataframe is None:
        raise ValueError("Please provide a dataframe")

    # first, check if individual count is numeric
    if 'individualCount' in dataframe.columns:
        errors = check_is_numeric(dataframe=dataframe,column_name='individualCount',errors=errors)

        if 'occurrenceStatus' in dataframe.columns:
            if any(dataframe[dataframe['individualCount'] == 0]):
                wrong_statuses = dataframe.loc[(dataframe['individualCount'] == 0) & (dataframe['occurrenceStatus'] != 'ABSENT')]
                if not wrong_statuses.empty:
                    errors.append('Some of your individual counts are 0, yet the occurrence status is set to present.  Please change occurrenceStatus to ABSENT')

    # first, check if both organismQuantity and organismQuantityType are present; if not, add error message
    if any(x in dataframe.columns for x in ['organismQuantity','organismQuantityType']):
        if not set(dataframe.columns).issuperset(['organismQuantity','organismQuantityType']):
            errors.append('You must include both organismQuantity and organismQuantityType.')

        # now, check each individually
        for var in ['organismQuantity','organismQuantityType']:
            if var in dataframe.columns:
                errors = check_is_string(dataframe=dataframe,column_name=var,errors=errors)
                errors = swap_error_message(errors=errors,
                                            orig_message='the {} column must be a string.'.format(var),
                                            new_message=unique_messages[var])
    
    # return errors
    if errors is not None:
        return errors
    return None