.. _What Does A Passing Occurrences Dataset Look Like?:

What Does A Passing Occurrences Dataset Look Like?
-------------------------------------------------------

If you've gone through all the steps outlined for the example 
occurrences dataset, your final step(s) will look like the following: 

.. prompt:: python

    >>> import pandas as pd
    >>> import corella
    >>>
    >>> occ = pd.read_csv('<NAME-OF-OCCURRENCES>.csv')
    >>> occ = corella.set_occurrences(dataframe=occ,basisOfRecord='HumanObservation',
    ...                               occurrenceStatus='PRESENT',occurrenceID=True,random_id=True)
    >>> occ = corella.set_scientific_name(dataframe=occ,scientificName='Species')
    >>> occ = corella.set_coordinates(dataframe=occ,decimalLatitude='Latitude',
    ...                               decimalLongitude='Longitude',geodeticDatum='WGS84',
    ...                               coordinatePrecision=0.1)
    >>> occ = corella.set_datetime(dataframe=occ,eventDate='Collection_date',
    ...                            string_to_datetime=True,yearfirst=False,dayfirst=True)
    >> corella.check_data(occurrences=occ)

And your final output from ``check_data()`` will look like this:

.. program-output:: python corella_user_guide/independent_observations/data_cleaning.py 39

`Back to Independent Observations TOC <index.html>`_