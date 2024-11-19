.. _use_occurrences:

use_occurrences
--------------------

One of the functions you can use to check your data is ``use_occurrences()``.  
This function aims to check that you have the following:

- ``basisOfRecord``: how the occurrence was recorded (was it observed by a human? machine? is it part of a collection?)
- ``occurrenceID`` or ``catalogNumber`` or ``recordNumber``: a unique identifier for the record
- ``occurrenceStatus`` (OPTIONAL): whether a species is present or absent.  Not required for data submission.

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

Initial run of ``use_occurrences``
======================================

Initally, we can run ``use_occurrences()`` to see what is in our dataset, 
and if any of the data types check with ``use_occurrences()`` are in there 
and correct.

.. prompt:: python

    >>> corella.use_occurrences(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 3

Here, we can see that we don't have any column names matching the Darwin 
Core standard, and must specify them to ``use_occurrences()`` to proceed.  
First, let's look at the ``basisOfRecord`` value.

specify ``basisOfRecord`` value
======================================

As mentioned above, the ``basisOfRecord`` value is a required and important 
field for an observation, as it lets others know how the record was recorded.  
For example, was it a machine that observed it? A human? Is this a specimen 
that's part of a collection?

Depending on your answer to these questions, the values will differ.  Luckily, 
Darwin Core has a predefined vocabulary to help you with this.  They are as 
follows:

.. program-output:: python corella_user_guide/bor_values.py

If you are not able to check these, or have mistyped one of them, ``use_occurrences()`` 
will provide the current accepted values for you as well:

.. prompt:: python

    >>> corella.use_occurrences(
    ...     dataframe=df,
    ...     basisOfRecord='observe'
    ... )

.. program-output:: python corella_user_guide/data_cleaning.py 4

For this exercise, let's assume a human has seen these, which equates to a value of 
``HumanObservation``.  We can then set the ``basisOfRecord`` argument as ``HumanObservation``, 
and it will, by default, set the value of ``basisOfRecord`` for the whole dataframe.

.. prompt:: python

    >>> corella.use_occurrences(
    ...     dataframe=df,
    ...     basisOfRecord='HumanObservation'
    ... )

.. program-output:: python corella_user_guide/data_cleaning.py 5

specify ``occurrenceStatus`` column
======================================

**Note:** This is an optional field, but we are including it here to share how this argument works, and how this will rename your column

Sometimes, you may want to include the ``occurrenceStatus`` field in your observations, especially 
if you were expecting to see a species in a particular area, and/or have seen them in the past but 
did not see them on that particular day, you can include this to say they were absent.

Since we have a column that denotes whether or not a species was present or absent, we can 
provide the name of that column, and ``corella`` will rename the column to conform with the 
Darwin Core standard.

.. prompt:: python

    >>> corella.use_occurrences(
    ...     dataframe=df,
    ...     basisOfRecord='HumanObservation',
    ...     occurrenceStatus='status'
    ... )

.. program-output:: python corella_user_guide/data_cleaning.py 6

generate occurrence IDs 
======================================

Every occurrence needs a unique identifier for easy future identification.  If your 
occurences don't have either an ``occurrenceID``, ``catalogNumber`` or ``recordNumber``, 
you can provide the boolean ``True`` argument to ``occurrenceID``, and unique identifiers 
will be generated for you.

**Note:** ``catalogNumber`` and / or ``recordNumber`` is normally used for collections, 
so it is best to go with ``occurrenceID`` if you're generating them using ``corella``.

.. prompt:: python

    >>> corella.use_occurrences(
    ...     dataframe=df,
    ...     basisOfRecord='HumanObservation',
    ...     occurrenceStatus='status',
    ...     occurrenceID=True
    ... )

.. program-output:: python corella_user_guide/data_cleaning.py 7

Now that we've taken care of the pieces of information ``use_occurrences()`` is responsible 
for, we can assign the new dataframe to a variable:

.. prompt:: python

    >>> df = corella.use_occurrences(
    ...     dataframe=df,
    ...     basisOfRecord='HumanObservation',
    ...     occurrenceStatus='status',
    ...     occurrenceID=True
    ... )

what does ``check_data`` and ``suggest_workflow`` say now? 
==============================================================

**Note:** each of the ``use_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now, we can check that our data column do comply with the Darwin Core standard.

.. prompt:: python

    >>> corella.check_data(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 8

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see how our data is doing this time round.

.. prompt:: python

    >>> corella.suggest_workflow(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 9