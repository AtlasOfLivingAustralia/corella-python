.. _use_scientific_name:

use_scientific_name
--------------------

One of the functions you can use to check certain columns of your data is ``use_scientific_name()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``scientificName``: the scientific name of the species you observed

It can also can check the following:

- ``scientificNameRank`` (OPTIONAL): rank of the scientific name you are providing.
- ``occurrenceStatus`` (OPTIONAL): whether a species is present or absent. 

For these examples, we will be using the following dataset:

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

If, however, you want to go through this workflow using your own data, please feel 
free to do so!  If your data is in a csv file, you can read your data into a ``pandas`` 
dataframe like so:

.. prompt:: python

    >>> import corella
    >>> import pandas as pd
    >>> df = pd.read_csv('<YOUR-FILENAME>.csv')

Initial run of ``use_scientific_name``
======================================

Initally, we can run ``use_scientific_name()`` to see what is in our dataset, 
and if any of the data types check with ``use_scientific_name()`` are in there 
and correct.

.. prompt:: python

    >>> corella.use_scientific_name(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 10

Here, we can see that we don't have any column names matching the Darwin 
Core standard, and must specify them to ``use_scientific_name()`` to proceed.  
The only required column is the ``scientificName`` value.

specifying ``scientificName``
======================================

Like with other ``use_*`` functions, to specify which column you want to rename or change, you 
specify it with the Darwin Core term.  In this case, it is ``scientificName``.

.. prompt:: python

    >>> corella.use_scientific_name(dataframe=df,scientificName='species')

.. program-output:: python corella_user_guide/data_cleaning.py 11

what does ``check_data`` and ``suggest_workflow`` say now? 
==============================================================

*Note:* each of the ``use_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> corella.check_data(occurrences=df)

.. program-output:: python corella_user_guide/data_cleaning.py 12

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> corella.suggest_workflow(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 13

To learn more about how to use these functions, go to 

- `use_occurrences <../use_occurrences.html>`_
- `use_coordinates <../use_coordinates.html>`_
- `use_datetime <../use_datetime.html>`_

Optional functions:

- `use_abundance <../use_abundance.html>`_
- `use_locality <../use_locality.html>`_