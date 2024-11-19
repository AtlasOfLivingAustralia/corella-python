.. _use_coordinates:

use_coordinates
--------------------

One of the functions you can use to check your data is ``use_coordinates()``.  
This function aims to check that you have the following:

- ``decimalLatitude``: the latitude of your observation
- ``decimalLongitude``: the latitude of your observation
- ``geodeticDatum``: the coordinate reference system (CRS) of your latitude and longitude

It can also (optionally) can check the following:

- ``coordinateUncertaintyInMeters``: uncertainty of your measurements in meters
- ``coordinatePrecision``: uncertainty of your measurements in decimal degrees

If you haven't read in our example dataset in the initial data cleaning page, 
here is an example and how to read it in:

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

If you wish to follow with your own dataset in a csv file, use ``pandas`` to read 
in your csv file:

.. prompt:: python

    >>> import pandas as pd
    >>> df = pd.read_csv('<YOUR-FILENAME>.csv')

Initial run of ``use_coordinates``
======================================

Initally, we can run ``use_coordinates()`` to see what is in our dataset, 
and if any of the data types check with ``use_coordinates()`` are in there 
and correct.

.. prompt:: python

    >>> corella.use_coordinates(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 12

Here, we can see that we don't have any column names matching the Darwin 
Core standard, and must specify them to ``use_coordinates()`` to proceed.  
The three required columns are ``decimalLatitude``, ``decimalLongitude``, 
and ``geodeticDatum``.

Second ``use_coordinates``
======================================

Initally, we can run ``use_coordinates()`` to see what is in our dataset, 
and if any of the data types check with ``use_coordinates()`` are in there 
and correct.

.. prompt:: python

    >>> corella.use_coordinates(dataframe=df,
    ...                         decimalLatitude='latitude',
    ...                         decimalLongitude='longitude')

.. program-output:: python corella_user_guide/data_cleaning.py 13

what does ``check_data`` and ``suggest_workflow`` say now? 
==============================================================

**Note:** each of the ``use_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> corella.check_data(occurrences=df)

#.. program-output:: python corella_user_guide/data_cleaning.py 10

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> corella.suggest_workflow(dataframe=df)

#.. program-output:: python corella_user_guide/data_cleaning.py 11