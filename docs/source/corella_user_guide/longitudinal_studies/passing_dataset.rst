.. _What Does A Passing Events Dataset Look Like?:

What Does A Passing Events Dataset Look Like?
-------------------------------------------------------

*Note: This next step assumes you have done all the steps in the below code*

.. dropdown:: Code for occurrences and events for example dataset

    .. prompt:: python

        >>> # this is each individual step as a command
        >>> import pandas as pd
        >>> import corella
        >>>
        >>> # first, events
        >>> events = pd.read_csv('<NAME-OF-EVENTSE>.csv')
        >>> events = corella.set_events(dataframe=events,
        ...                             eventType='type',
        ...                             samplingProtocol='Observation',
        ...                             Event='name',
        ....                            event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
        >>> events = corella.set_datetime(dataframe=events,
        ...                               eventDate='date',
        ...                               string_to_datetime=True,
        ...                               yearfirst=False,
        ...                               dayfirst=True)
        >>> events = corella.set_locality(dataframe=events,
        >>>                               locality='location')
        >>>
        >>> # now, set_occurrences
        >>> occ = pd.read_csv('<NAME-OF-OCCURRENCES>.csv')
        >>> occ = corella.set_scientific_name(dataframe=occ,
        ...                                   scientificName='Species')
        >>> occ = corella.set_coordinates(dataframe=occ,
        ...                               decimalLatitude='Latitude',
        ...                               decimalLongitude='Longitude',
        ...                               geodeticDatum='WGS84',
        ...                               coordinatePrecision=0.1)
        >>> occ = corella.set_datetime(dataframe=occ,
        ...                            eventDate='Collection_date',
        ...                            string_to_datetime=True,
        ...                            yearfirst=False,
        ...                            dayfirst=True)
        >>> corella.set_occurrences(dataframe=occ,
        ...                         add_eventID=True,
        ...                         occurrenceStatus='PRESENT',
        ...                         occurrenceID=True,
        ...                         add_eventID=True,
        ...                         events=events,
        ...                         eventType='Observation')

Before you write your metadata using ``paperbark`` or package your Darwin Core Archive using ``galaxias``, 
run ``check_data()`` for the final time.

.. prompt:: python

    >> corella.check_data(occurrences=occ,
    ...                   events=events)

If everything passes, you will get the following output:

.. program-output:: python corella_user_guide/longitudinal_studies/events_workflow.py 16

`Back to Longitudinal Studies TOC <index.html>`_