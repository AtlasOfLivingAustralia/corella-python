.. _set_scientific_name:

set_scientific_name
--------------------

One of the functions you can use to check certain columns of your data is ``set_scientific_name()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``scientificName``: the scientific name of the species you observed

It can also can check the following:

- ``scientificNameRank`` (OPTIONAL): rank of the scientific name you are providing.
- ``scientificNameAuthorship`` (OPTIONAL): Authors of the species name you are using.

specifying ``scientificName``
---------------------------------------

Like with other ``set_*`` functions, to specify which column you want to rename or change, you 
specify it with the Darwin Core term.  In this case, it is ``scientificName``.

.. prompt:: python

    >>> corella.set_scientific_name(dataframe=occ,scientificName='Species')

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 11

what does ``check_data`` and ``suggest_workflow`` say now? 
------------------------------------------------------------------

*Note:* each of the ``set_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> occ = corella.set_scientific_name(dataframe=occ,scientificName='Species')
    >>> corella.check_data(occurrences=occ)

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 12

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> corella.suggest_workflow(dataframe=occ)

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 13

Other functions
---------------------------------------

To learn more about how to use these functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_

Optional functions:

- `set_abundance <set_abundance.html>`_
- `set_locality <set_locality.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_