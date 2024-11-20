.. _use_locality:

use_locality
--------------------

One of the functions you can use to check your data is ``use_locality()``.  
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