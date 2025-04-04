.. _set_locality:

set_locality
--------------------

**Note: the information here is not required by the ALA**

One of the functions you can use to check your data is ``set_locality()``.  
This function aims to check if you have the following:

- ``continent``: the latitude of your observation
- ``country``: the latitude of your observation
- ``countryCode``: the coordinate reference system (CRS) of your latitude and longitude
- ``stateProvince``: uncertainty of your measurements in meters
- ``locality``: uncertainty of your measurements in decimal degrees

specifying ``continent`` and ``country``
--------------------------------------------

.. prompt:: python

    >>> corella.set_locality(dataframe=occ,continent='Australia')

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 29

However, for Darwin Core purposes, ``Australia`` is a country, and ``Oceania`` is the 
continent that Australia is part of.  Therefore, we can set ``continent='Oceania'`` and 
``country='Australia'``.

.. prompt:: python

    >>> corella.set_locality(dataframe=occ,continent='Oceania',country='Australia')

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 30

Other functions
---------------------------------------

To learn more about how to use other functions, go to 

- `set_occurrences <set_occurrences.html>`_
- `set_coordinates <set_coordinates.html>`_
- `set_datetime <set_datetime.html>`_
- `set_scientific_name <set_scientific_name.html>`_

Optional functions:

- `set_abundance <set_abundance.html>`_

Passing Dataset:

- `Passing Dataset <passing_dataset.html>`_