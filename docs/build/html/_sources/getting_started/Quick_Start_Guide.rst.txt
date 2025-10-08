Quick start guide
=====================

*Dax Kellie, Amanda Buyan*

``corella`` is a tool for standardising data in Python to use the Darwin Core Standard. 
Darwin Core Standard is the primary data standard for species occurrence data—records of 
organisms observed in a location and time—in the Atlas of Living Australia (ALA), other 
Living Atlases and the Global Biodiversity Information Facility (GBIF). The standard allows 
the ability to compile data from a variety of sources, improving the ease to share, use 
and reuse data.

The main tasks to standardise data with Darwin Core Standard are:

- Ensure columns use valid Darwin Core terms as column names
- Include all required information (e.g. scientific name, unique observation ID, valid date)
- Ensure columns contain valid data
- This process can be daunting. corella is designed to reduce confusion of how to get started, and help determine which Darwin Core terms might match your column names.

Install
-------------

See `<Installation Instructions <Installation.html>`_.

To load the package:

.. prompt:: Python

    >>> import corella

Rename, add or edit columns
-------------------------------

Here is a minimal example dataset of cockatoo observations. In our dataframe, 
``df``, there are columns that contain information that we would like to standardise 
using Darwin Core.


.. prompt:: Python

    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'latitude': [-35.310, "-35.273"], # deliberate error for demonstration purposes
    ...     'longitude': [149.125, 149.133],
    ...     'date': ["14-01-2023", "15-01-2023"],
    ...     'time': ["10:23:00", "11:25:00"],
    ...     'month': ["January", "February"],
    ...     'day': [100, 101],
    ...     'species': ["Callocephalon fimbriatum", "Eolophus roseicapilla"],
    ...     'n': [2, 3],
    ...     'crs': ["WGS84", "WGS8d"],
    ...     'country': ["Australia", "Denmark"],
    ...     'continent': ["Oceania", "Europe"]
    ... })
    >>> df

.. program-output:: python getting_started/quick_start_code.py 1

We can standardise our data with ``set_`` functions. The ``set_`` functions possess a suffix name 
to identify what type of data they are used to standardise (e.g. ``set_coordinates``, ``set_datetime``), 
and arguments in ``set_`` functions are valid Darwin Core terms (ie column names). By grouping Darwin 
Core terms based on their data type, corella makes it easier for users to find relevant Darwin Core 
terms to use as column names (one of the most onerous parts of Darwin Core for new users).

Let’s specify that the scientific name (i.e. genus + species name) in our data is in the species 
column by using ``set_scientific_name()``. You’ll notice 2 things happen:

- The species column in our dataframe is renamed to ``scientificName``
- ``set_scientific_name()`` runs a check on our species column to make sure it is formatted correctly

.. prompt:: Python

    >>> df_dwc = corella.set_scientific_name(dataframe=df,scientificName='species')
    >>> df_dwc

.. program-output:: python getting_started/quick_start_code.py 2

What happens when we add a column with an error in it? The ``latitude`` column in ``df`` is a class 
``string`` column, instead of a numeric column as it should be. When we try to update the column 
name using ``set_coordinates()``, an error tells us the class is wrong.

.. prompt:: Python

    >>> df_dwc = corella.set_coordinates(dataframe=df_dwc,
    ...                                  decimalLongitude = 'longitude',
    ...                                  decimalLatitude = 'latitude')

.. program-output:: python getting_started/quick_start_code.py 3

Fix or update columns
--------------------------
To change, edit or fix a column, users can edit the column within the ``set_`` function.

Each ``set_`` function is essentially a specialised ``pandas`` ``rename`` function, meaning 
users can edit columns using the same processes they would when using ``pandas.rename``. We 
can fix the latitude column so that it is class numeric within the ``set_coordinates()`` function.

.. prompt:: Python

    >>> df_dwc['latitude'] = pd.to_numeric(df_dwc['latitude'])
    >>> df_dwc = corella.set_coordinates(dataframe=df_dwc,
    ...                                  decimalLongitude = 'longitude',
    ...                                  decimalLatitude = 'latitude')
    >>> df_dwc

.. program-output:: python getting_started/quick_start_code.py 4

Auto-detect columns
----------------------
``corella`` is also able to detect when a column exists in a data frame that already has 
a valid Darwin Core term as a column name. For example, ``df`` contains columns with 
locality information. We can use ``set_locality()`` to identify these columns, but because 
several columns already have valid Darwin Core terms as column names (``country`` and ``continent``), 
``set_locality()`` will detect these valid Darwin Core columns in ``df`` and check them automatically.

.. prompt:: Python

    >>> df_dwc = corella.set_locality(dataframe=df)

.. program-output:: python getting_started/quick_start_code.py 4

``corella``’s auto-detection prevents users from needing to specify every single column, reducing 
the amount of typing for users when they have already have valid Darwin Core column names!

Suggest a workflow
------------------------
Unsure where to start? Confused about the minimum requirements to share your data? Using 
``suggest_workflow()`` is the easiest way to get started in ``corella``.

``suggest_workflow()`` provides a high level summary designed to show:

- Which column names match valid Darwin Core terms
- The minimum requirements for data in a Darwin Core Archive (i.e. a completed data resource in Darwin Core standard).
- A suggested workflow to help you add the minimum required columns
- Additional functions that could be added to a piped workflow (based the provided dataset’s matching Darwin Core column names)

The intention of ``suggest_workflow()`` is to provide a general help function whenever users feel uncertain about what to do next. Let’s see what the output says about our original dataframe df.

.. prompt:: Python

    >>> corella.suggest_workflow(occurrences=df)

.. program-output:: python getting_started/quick_start_code.py 5

``suggest_workflow()`` will update the suggested function pipe to only suggest functions 
that are necessary to standardise your data correctly.

For example, after using one of the suggested functions ``set_occurrences()``, if we run 
``suggest_workflow()`` again, the output message no longer suggests ``set_occurrences()``.

.. prompt:: Python

    >>> df_edited = corella.set_occurrences(occurrences=df,
    ...                                     occurrenceID='sequential',
    ...                                     basisOfRecord='HumanObservation')
    >>> corella.suggest_workflow(occurrences=df_edited)

.. program-output:: python getting_started/quick_start_code.py 6

Test your data
----------------------
If your dataset already uses valid Darwin Core terms as column names, instead of 
working through each ``set_`` function, you might wish to run tests on your entire dataset. 
To run checks on your data like a test suite, use ``check_dataset()``. ``check_dataset()`` 
runs the relevant check on each matching Darwin Core column and returns a summary of the 
results, along with any error messages returned by those checks.

.. prompt:: Python

    >>> df = pd.DataFrame({
    ...     'latitude': [-35.310, "-35.273"], # deliberate error for demonstration purposes
    ...     'longitude': [149.125, 149.133],
    ...     'date': ["14-01-2023", "15-01-2023"],
    ...     'individualCount': [0, 2],
    ...     'species': ["Callocephalon fimbriatum", "Eolophus roseicapilla"],
    ...     'country': ["AU", "AU"],
    ...     'occurrenceStatus': ["present", "present"],
    ... })
    >>> corella.check_dataset(occurrences=df)

.. program-output:: python getting_started/quick_start_code.py 7

The goal of ``check_dataset()`` is to make running many checks more efficient, and 
to cater to users who prefer a test-suite-like workflow.