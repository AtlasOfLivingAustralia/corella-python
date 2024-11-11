import pandas as pd
from pandas.api.types import is_numeric_dtype,is_string_dtype,is_datetime64_any_dtype

def snake_to_camel_case(list_of_words=None):
    """
    Changes snake case to camel case.

    Parameters
    ----------
        list_of_words: ``list``
            list of words to switch case

    Returns
    -------
        New list with the changed case
    """
    new_list = []
    for w in list_of_words:
        term = w.lower().split("_")
        for i in range(len(term)):
            term[i] = term[i].capitalize()
        new_list.append("".join(term))
    return new_list

def check_is_string(dataframe=None,
                    column_name=None,
                    errors=None):
    """
    Checks whether or not your chosen column has data with the string type.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            dataframe with data to check
        column_name: ``str``
            name of column to check
        errors: ``list``
            current list of errors

    Returns
    -------
        ``errors``: ``list``
            updated list of errors
    """
    if not is_string_dtype(dataframe[column_name]):
        errors.append('the {} column must be a string.'.format(column_name))
    return errors

def check_is_numeric(dataframe=None,
                     column_name=None,
                     errors=None):
    """
    Checks whether or not your chosen column has data with the numeric type.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            dataframe with data to check
        column_name: ``str``
            name of column to check
        errors: ``list``
            current list of errors

    Returns
    -------
        ``errors``: ``list``
            updated list of errors
    """
    if not is_numeric_dtype(dataframe[column_name]):
        errors.append('the {} column must be numeric.'.format(column_name))
    return errors

def check_is_datetime(dataframe=None,
                     column_name=None,
                     errors=None):
    """
    Checks whether or not your chosen column has data with the numeric type.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            dataframe with data to check
        column_name: ``str``
            name of column to check
        errors: ``list``
            current list of errors

    Returns
    -------
        ``errors``: ``list``
            updated list of errors
    """
    if not is_datetime64_any_dtype(dataframe[column_name]):
        errors.append('the {} column must be in datetime format.'.format(column_name))
    return errors

def swap_error_message(errors=None,
                       orig_message=None,
                       new_message=None):
    """
    Swaps generic error with custom error message

    Parameters
    ----------
        errors: ``list``
            list of errors to check for messages
        orig_message: ``str``
            original message in ``errors`` list
        new_message: ``str``
            new message in place of ``orig_message``

    Returns
    -------
        updated list of errors
    """
    if orig_message in errors:
        index = errors.index(orig_message)
        errors[index] = new_message
    return errors

def get_bor_values():
    """
    Gets current valid values for ``basisOfRecord``

    Parameters
    ----------
        None

    Returns
    -------
        A list of valid ``basisOfRecord`` terms 
    """
    temp = pd.read_table('https://raw.githubusercontent.com/gbif/parsers/dev/src/main/resources/dictionaries/parse/basisOfRecord.tsv').dropna()
    terms = list(set(temp['PRESERVED_SPECIMEN']))
    terms = snake_to_camel_case(terms)
    return terms