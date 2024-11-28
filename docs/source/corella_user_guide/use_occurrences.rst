.. _use_occurrences:

use_occurrences
--------------------

One of the functions you can use to check certain columns of your data is ``use_occurrences()``.  
This function aims to check that you have the following Darwin Core Vocabulary Terms:

- ``basisOfRecord``: how the occurrence was recorded (was it observed by a human? machine? is it part of a collection?)
- ``occurrenceID`` or ``catalogNumber`` or ``recordNumber``: a unique identifier for the record (only one of these is necessary)
- ``occurrenceStatus`` (OPTIONAL): whether a species is present or absent.  Not required for data submission.

For these examples, we will be using the following dataset:

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

If, however, you want to go through this workflow using your own data, please feel 
free to do so!  If your data is in a csv file, you can read your data into a ``pandas`` 
dataframe like so:

.. prompt:: python

    >>> import corella
    >>> import pandas as pd
    >>> df = pd.read_csv('<YOUR-FILENAME>.csv')

Initial run of ``use_occurrences``
======================================

Initally, let's run ``use_occurrences()`` to see if any of our columns match the Darwin 
Core Vocabulary mentioned above:

.. prompt:: python

    >>> corella.use_occurrences(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 3

Here, we can see that we don't have any column names matching ``basisOfRecord``, ``occurrenceStatus``, 
``occurrenceID``, ``catalogNumber`` or ``recordNumber``.  Luckily, there are options in ``use_occurrences()`` 
that allow the user to specify a column of data as one of the column names, or to set a default value for 
the column.

Specifying ``basisOfRecord`` value
======================================

As mentioned above, the ``basisOfRecord`` value is a required and important 
field for an observation, as it lets others know how the record was recorded.  
For example, was it a machine that observed it? A human? Is this a specimen 
that's part of a collection?

Depending on your answer to these questions, the information you provide will differ.  
Luckily, Darwin Core has a predefined vocabulary to help you with this.  The current 
accepted values are as follows:

.. program-output:: python corella_user_guide/bor_values.py

For this exercise, let's assume a human has seen these, which equates to a value of 
``HumanObservation``.  We can then set the ``basisOfRecord`` argument as ``HumanObservation``, 
and it will, by default, set the value of ``basisOfRecord`` for the whole dataframe.

.. prompt:: python

    >>> corella.use_occurrences(
    ...     dataframe=df,
    ...     basisOfRecord='HumanObservation'
    ... )

.. program-output:: python corella_user_guide/data_cleaning.py 5

How to generate occurrence IDs 
======================================

*Note:* If you have occurrence IDs already in your dataset, you can specify the name of the column 
that contains your IDs, and ``corella`` will rename that column to comply with the Darwin Core Vocabulary 
Standard.

*Note:* ``catalogNumber`` and / or ``recordNumber`` is normally used for collections, 
so it is best to go with ``occurrenceID`` if you're generating them using ``corella``.

Every occurrence needs a unique identifier for easy future identification.  If your 
occurences don't have either an ``occurrenceID``, ``catalogNumber`` or ``recordNumber``, 
you can provide a value of ``True`` to the ``occurrenceID``, and unique identifiers 
will be generated for you.

.. prompt:: python

    >>> corella.use_occurrences(
    ...     dataframe=df,
    ...     basisOfRecord='HumanObservation',
    ...     occurrenceStatus='status',
    ...     occurrenceID=True
    ... )

.. program-output:: python corella_user_guide/data_cleaning.py 7

specify ``occurrenceStatus`` column
======================================

*Note:* This is an optional field, but we are including it here to share how this argument works, and how this will rename your column

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

what does ``check_data`` and ``suggest_workflow`` say now? 
==============================================================

*Note:* each of the ``use_*`` functions checks your data for compliance with the 
Darwin core standard, but it's always good to double-check your data.

Now that we've taken care of the pieces of information ``use_occurrences()`` is responsible 
for, we can assign the new dataframe to a variable:

.. prompt:: python

    >>> df = corella.use_occurrences(
    ...     dataframe=df,
    ...     basisOfRecord='HumanObservation',
    ...     occurrenceStatus='status',
    ...     occurrenceID=True
    ... )

Now, we can check that this new dataframe complies with the Darwin Core standard for the ``basisOfRecord``, 
``occurrenceStatus``, ``occurrenceID``, ``catalogNumber`` and ``recordNumber`` columns.

.. prompt:: python

    >>> corella.check_data(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 8

However, since we don't have all of the required columns, we can run ``suggest_workflow()`` 
again to see what other functions we can use to check our data:

.. prompt:: python

    >>> corella.suggest_workflow(dataframe=df)

.. program-output:: python corella_user_guide/data_cleaning.py 9

To learn more about how to use these functions, go to 

- `use_coordinates <../use_coordinates.html>`_
- `use_datetime <../use_datetime.html>`_
- `use_scientific_name <../use_scientific_name.html>`_

Optional functions:

- `use_abundance <../use_abundance.html>`_
- `use_locality <../use_locality.html>`_