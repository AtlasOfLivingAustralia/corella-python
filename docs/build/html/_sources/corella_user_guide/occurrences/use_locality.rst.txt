.. _use_locality:

use_locality
--------------------

**Note: the information here is not required by the ALA**

One of the functions you can use to check your data is ``use_locality()``.  
This function aims to check if you have the following:

- ``continent``: the latitude of your observation
- ``country``: the latitude of your observation
- ``countryCode``: the coordinate reference system (CRS) of your latitude and longitude
- ``stateProvince``: uncertainty of your measurements in meters
- ``locality``: uncertainty of your measurements in decimal degrees

If you haven't read in our example dataset in the initial data cleaning page, 
here is an example and how to read it in:

.. prompt:: python

    >>> import corella
    >>> import pandas as pd
    >>> occ = pd.DataFrame(
    ...     {'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
    ...     'latitude': [-35.310, '-35.273'], 
    ...     'longitude': [149.125, 149.133], 
    ...     'date': ['14-01-2023', '15-01-2023'], 
    ...     'status': ['present', 'present']}
    ... )

If you wish to follow with your own dataset in a csv file, use ``pandas`` to read 
in your csv file:

.. prompt:: python

    >>> import pandas as pd
    >>> occ = pd.read_csv('<YOUR-FILENAME>.csv')

Initial run of ``use_locality()``
---------------------------------------

Initally, we can run ``use_locality()`` to see what is in our dataset, 
and if any of the data types check with ``use_locality()`` are in there 
and correct.

.. prompt:: python

    >>> corella.use_locality(dataframe=occ)

.. program-output:: python corella_user_guide/occurrences/data_cleaning.py 28

We can see that we don't have any extra locality information.  However, we can always 
add it in.  For example, we know that these occurrences happened in Australia.  We may 
then want to put the continent as ``Australia``.

specifying ``continent`` and ``country``
--------------------------------------------

.. prompt:: python

    >>> corella.use_locality(dataframe=occ,continent='Australia')

.. program-output:: python corella_user_guide/occurrences/data_cleaning.py 29

However, for Darwin Core purposes, ``Australia`` is a country, and ``Oceania`` is the 
continent that Australia is part of.  Therefore, we can set ``continent='Oceania'`` and 
``country='Australia'``.

.. prompt:: python

    >>> corella.use_locality(dataframe=occ,continent='Oceania',country='Australia')

.. program-output:: python corella_user_guide/occurrences/data_cleaning.py 30

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `use_occurrences <use_occurrences.html>`_
- `use_coordinates <use_coordinates.html>`_
- `use_datetime <use_datetime.html>`_
- `use_scientific_name <use_scientific_name.html>`_

Optional functions:

- `use_abundance <use_abundance.html>`_