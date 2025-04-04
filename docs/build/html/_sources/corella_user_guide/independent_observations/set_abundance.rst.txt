.. _set_abundance:

set_abundance
--------------------

**Note: the information here is not required by the ALA**

One of the functions you can use to check your data is ``set_abundance()``.  
This function aims to check that you have the following:

- ``individualCount``: the number of individuals observed of a particular species

It can also (optionally) can check the following:

- ``organismQuantity``: a description of your individual counts
- ``organismQuantityType``: describes what your organismQuantity is

For this exercise, will use a very small dataframe with a column ``'count'``, which denotes 
the number of individuals observed:

.. prompt:: python

    >>> import corella
    >>> import pandas as pd
    >>> occ = pd.DataFrame(
    ...     {'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
    ...     'latitude': [-35.310, '-35.273'], 
    ...     'longitude': [149.125, 149.133], 
    ...     'date': ['14-01-2023', '15-01-2023'], 
    ...     'status': ['present', 'present'],
    ...     'count': [2,1]}
    ... )

specifying ``individualCount``
-----------------------------------------

.. prompt:: python

    >>> corella.set_abundance(dataframe=occ,individualCount='count')

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 27

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_
- `set_scientific_name <set_scientific_name.html>`_

Optional functions:

- `set_locality <set_locality.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_