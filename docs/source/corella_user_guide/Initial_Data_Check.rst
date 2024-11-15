.. _Initial Data Check:

Initial Data Check
--------------------

To get started, if you think that your data is ready to go, you 
can read in your data and use ``corella.check_data()``.  To read 
in your data from a csv file, you can use ``pandas`` to do this:

.. prompt:: python

    >>> import pandas as pd
    >>> df = pd.read_csv('<YOUR-FILENAME>.csv')

However, for these examples, we will be using a smaller dataset 
as shown below:

.. prompt:: python

    >>> import corella
    >>> import pandas as pd
    >>> df = pd.DataFrame(
    ...     {'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
    ...     'latitude': [-35.310, '-35.273'], 
    ...     'longitude': [149.125, 149.133], 
    ...     'date': ['14-01-2023', '15-01-2023'], 
    ...     'status': ['present', 'present']}
    ... )
    >>> corella.check_data(occurrences=df)

.. program-output:: python corella_user_guide/data_cleaning.py 1

For this first example, the data tests may not be showing any errors, but 
no column names were checked.  This is because the names of the columns are 
not part of the standard Darwin Core vocabulary.  However, we have created a 
series of functions that can help you get your data conformant with the 
Darwin Core standard.  To show the functions you will need to do this, we 
have developed an all-purpose command called ``suggest_workflow()``.  Here 
are the results of this particular dataset:                                  

.. prompt:: python

    >>> corella.suggest_workflow(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 2