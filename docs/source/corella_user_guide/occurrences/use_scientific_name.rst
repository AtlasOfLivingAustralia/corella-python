.. _use_scientific_name:

use_scientific_name
--------------------

One of the functions you can use to check certain columns of your data is ``use_scientific_name()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``scientificName``: the scientific name of the species you observed

It can also can check the following:

- ``scientificNameRank`` (OPTIONAL): rank of the scientific name you are providing.
- ``scientificNameAuthorship`` (OPTIONAL): Authors of the species name you are using.

Initial run of ``use_scientific_name``
---------------------------------------

Initally, we can run ``use_scientific_name()`` to see what is in our dataset, 
and if any of the data types check with ``use_scientific_name()`` are in there 
and correct.

.. prompt:: python

    >>> corella.use_scientific_name(dataframe=df)

.. program-output:: python corella_user_guide/occurrences/data_cleaning.py 10

Here, we can see that we don't have any column names matching the Darwin 
Core standard, and must specify them to ``use_scientific_name()`` to proceed.  
The only required column is the ``scientificName`` value.

specifying ``scientificName``
---------------------------------------

Like with other ``use_*`` functions, to specify which column you want to rename or change, you 
specify it with the Darwin Core term.  In this case, it is ``scientificName``.

.. prompt:: python

    >>> corella.use_scientific_name(dataframe=df,scientificName='Species')

.. program-output:: python corella_user_guide/occurrences/data_cleaning.py 11

what does ``check_data`` and ``suggest_workflow`` say now? 
------------------------------------------------------------------

*Note:* each of the ``use_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> df = corella.use_scientific_name(dataframe=df,scientificName='Species')
    >>> corella.check_data(occurrences=df)

.. program-output:: python corella_user_guide/occurrences/data_cleaning.py 12

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> corella.suggest_workflow(dataframe=df)

.. program-output:: python corella_user_guide/occurrences/data_cleaning.py 13

Other functions
---------------------------------------

To learn more about how to use these functions, go to 

- `use_occurrences <use_occurrences.html>`_
- `use_coordinates <use_coordinates.html>`_
- `use_datetime <use_datetime.html>`_

Optional functions:

- `use_abundance <use_abundance.html>`_
- `use_locality <use_locality.html>`_