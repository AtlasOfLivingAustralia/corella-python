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

.. program-output:: python corella_user_guide/data_cleaning.py 14

Here, we can see that we don't have any column names matching the Darwin 
Core standard, and must specify them to ``use_coordinates()`` to proceed.  
The three required columns are ``decimalLatitude``, ``decimalLongitude``, 
and ``geodeticDatum``.

Specifying ``decimalLatitude`` and ``decimalLongitude``
==========================================================

Since we have latitude and longitude columns, we can specify them in the 
``use_coordinates()`` function, and the columns will be renamed and the 
values checked to see if i) they are numeric; and ii) if they are in the 
correct ranges.

.. prompt:: python

    >>> corella.use_coordinates(dataframe=df,
    ...                         decimalLatitude='latitude',
    ...                         decimalLongitude='longitude')

.. program-output:: python corella_user_guide/data_cleaning.py 15

As we can see here, there are some values that are not numeric.  Luckily, 
``pandas`` has a function called ``to_numeric`` which will convert strings 
to numeric values for you (assuming those strings are numbers).  Below is an 
example of how to convert a column to all numeric values.  Now that the values 
are all numeric and in the correct range, we will get an updated dataframe.

.. prompt:: python

    >>> df['latitude'] = pd.to_numeric(df['latitude'])
    >>> corella.use_coordinates(dataframe=df,
    ...                         decimalLatitude='latitude',
    ...                         decimalLongitude='longitude')

.. program-output:: python corella_user_guide/data_cleaning.py 16

``geodeticDatum``
======================================

Another required field is called ``geodeticDatum``.  This column is required as 
it lets others know how you measured latitude and longitude.  ``geodeticDatum`` 
refers to a Coordinate Reference System (CRS), which is how three-dimensional 
coordinates are represented on a two-dimensional surface.  The most common CRS 
(and what GPSs, as well as the ALA, uses) is called WGS84.  If you know that this 
is the CRS you have used, you can set the default value of ``geodeticDatum`` in 
``use_coordinates()``.

.. prompt:: python

    >>> corella.use_coordinates(dataframe=df,
    ...                         decimalLatitude='latitude',
    ...                         decimalLongitude='longitude',
    ...                         geodeticDatum='WGS84')

.. program-output:: python corella_user_guide/data_cleaning.py 17

Adding Uncertainty
======================================

There is always uncertainty in measurements of latitude and longitude; however, 
sometimes it is useful to include this, especially if you know the uncertainty of 
your instruments or measurements.  If you know this information and want to include 
it, you can specify a default value (similar to the ``geodeticDatum`` column above) 
to either ``coordinatePrecision`` or ``coordinateUncertaintyInMeters``.  The former is 
in decimal degrees, and the latter is in meters.

.. prompt:: python

    >>> corella.use_coordinates(dataframe=df,
    ...                         decimalLatitude='latitude',
    ...                         decimalLongitude='longitude',
    ...                         geodeticDatum='WGS84',
    ...                         coordinatePrecision=0.1)

.. program-output:: python corella_user_guide/data_cleaning.py 18

what does ``check_data`` and ``suggest_workflow`` say now? 
==============================================================

**Note:** each of the ``use_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> corella.check_data(occurrences=df)

.. program-output:: python corella_user_guide/data_cleaning.py 19

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> corella.suggest_workflow(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 20