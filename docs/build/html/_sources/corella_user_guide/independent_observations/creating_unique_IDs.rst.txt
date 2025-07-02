.. _creating_unique_IDs:

Creating Unique IDs
---------------------------

Having a unique ID for each occurrence/event is useful because these unique IDs can identify 
individual observations, and make it possible to change, amend or delete observations over time. 
They also prevent accidental deletion when when more than one record contains the same 
information (and would otherwise be considered a duplicate).

There are three ways you can create identifiers for your occurrences/events: 

- random IDs
- sequential IDs
- composite IDs

random IDs
=============

Random IDs are created automatically in ``corella`` using the `uuid package <https://pypi.org/project/uuid/>`_.  
To automatically generate random IDs, set ``occurrenceID='random'`` like so:

.. prompt:: python

    >>> occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
    ...                     'latitude': [-35.310, -35.273], 
    ...                     'longitude': [149.125, 149.133], 
    ...                     'date': ['14-01-2023', '15-01-2023']})
    >>> occ = corella.set_occurrences(dataframe=occ,occurrenceID='random')
    >>> occ

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 35

sequential IDs
==================

Sequential IDs are created from 0 to the number of rows in the data frame.  Like above, to generate sequential 
ids, set ``occurrenceID='sequential'``.

.. prompt:: python

    >>> occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
    ...                     'latitude': [-35.310, -35.273], 
    ...                     'longitude': [149.125, 149.133], 
    ...                     'date': ['14-01-2023', '15-01-2023']})
    >>> occ = corella.set_occurrences(dataframe=occ,occurrenceID='sequential')
    >>> occ

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 36

composite IDs
==================

If you don't want only UUIDs or sequential IDs, but a composite of multiple items, you can provide a list of 
column names and keywords in the order you want to compose your unique ID. Below are examples using the ``'date'`` 
column in conjunction with either the keywords ``sequential`` or ``random`` to add either sequential or random 
IDs to your composite ID.

.. prompt:: python

    >>> occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
    ...                     'latitude': [-35.310, -35.273], 
    ...                     'longitude': [149.125, 149.133], 
    ...                     'date': ['14-01-2023', '15-01-2023']})
    >>> occ = corella.set_occurrences(dataframe=occ,occurrenceID=['sequential','date'])
    >>> occ

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 37

.. prompt:: python

    >>> occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
    ...                     'latitude': [-35.310, -35.273], 
    ...                     'longitude': [149.125, 149.133], 
    ...                     'date': ['14-01-2023', '15-01-2023']})
    >>> occ = corella.set_occurrences(dataframe=occ,occurrenceID=['date','random'])
    >>> occ

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 38

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_
- `set_scientific_name <set_scientific_name.html>`_

Optional functions:

- `set_abundance <set_abundance.html>`_
- `set_collection <set_collection.html>`_
- `set_individual_traits <set_individual_traits.html>`_
- `set_license <set_license.html>`_
- `set_locality <set_locality.html>`_
- `set_taxonomy <set_taxonomy.html>`_

Creating Unique IDs:

- `Creating Unique IDs for your Occurrences <creating_unique_IDs.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_