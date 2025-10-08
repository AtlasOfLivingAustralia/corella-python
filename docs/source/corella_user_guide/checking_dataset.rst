:orphan:

Checking your dataset
==========================

*Dax Kellie, Amanda Buyan*

A Darwin Core Archive consists of several pieces to ensure a dataset is structured correctly 
(and can be restructured correctly in the future). These pieces include the dataset, a metadata 
statement, and an xml file detailing how the columns in the data relate to each other.

``corella`` is designed to check whether a dataset conforms to Darwin Core standard. This involves 
two main steps: 

- Ensuring that a dataset uses valid Darwin Core terms as column names 
- Checking that the data in each column is the correct type for the specified Darwin Core term

This vignette gives additional information about the second step of checking each column’s data.

Checking individual terms
------------------------------
``corella`` consists of many internal ``check_`` functions. Each one runs basic validation checks on 
the specified column to ensure the data conforms to the Darwin Core term’s expected data type.

For example, here is a very small dataset with two observations of galahs (*Eolophus roseicapilla*) 
(class ``str``), their latitude and longitude coordinates (class ``numeric``), and a location description 
in the column place (class ``str``).

.. prompt:: Python

    >>> import corella
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'name': ['Eolophus roseicapilla', 'Eolophus roseicapilla'],
    ...     'latitude': [-35.310, -35.273],
    ...     'longitude': [149.125, 149.133],
    ...     'place': ['a big tree', 'an open field'],
    ... })
    >>> df

.. program-output:: python corella_user_guide/checking_dataset_code.py 1

I can use the function ``set_coordinates()`` to specify which of my columns refer to 
the valid Darwin Core terms ``decimalLatitude`` and ``decimalLongitude``. I have intentionally 
added the wrong column place as ``decimalLatitude``. ``corella`` will return an error because 
``decimalLatitude`` and ``decimalLongitude`` fields must be numeric in Darwin Core standard. 
This error comes from a small internal checking function called ``check_decimalLatitude()``.

.. prompt:: Python

    >>> df = corella.set_coordinates(dataframe=df,
    ...                              decimalLatitude = 'place', # wrong column
    ...                              decimalLongitude = 'longitude')

.. program-output:: python corella_user_guide/checking_dataset_code.py 2

Supported terms
-----------------------
``corella`` contains internal ``check_`` functions for all individual Darwin Core terms 
that are supported. These are as follows:

.. dropdown:: Supported Darwin Core Terms and Their Associated Functions 
    :color: info
    
    .. csv-table:: 
        :file: ../corella_user_guide/data/supported-terms.csv
        :widths: 20, 40  
        :header-rows: 1

When a user specifies a column to a matching Darwin Core term (or the column/term is detected by 
``corella`` automatically) in a ``set_`` function, the ``set_`` function triggers that matching 
term’s ``check_`` function. This process ensures that the data is correctly formatted prior to 
being saved in a Darwin Core Archive.

It’s useful to know that these internal, individual ``check_`` functions exist because they are 
the building blocks of a full suite of checks, which users can run with ``check_dataset()``.

Checking a full dataset
----------------------------
For users who are familiar with Darwin Core standards, or who have datasets that already conform 
to Darwin Core standards (or are very close), it might be more convenient to run many checks at one time.

Users can use the ``check_dataset()`` function to run a “test suite” on their dataset. ``check_dataset()`` 
detects all columns that match valid Darwin Core terms, and runs all matching ``check_`` functions all at 
once, interactively.

The output of ``check_dataset()`` returns: 

- A summary table of whether each matching column’s check passed or failed 
- The number of errors and passed columns 
- Whether the data meets minimum Darwin Core requirements 
- The first 5 error messages returned by checks

.. prompt:: Python

    >>> df = pd.DataFrame({
    ...     'decimalLatitude': [-35.310, "-35.273"], # deliberate error for demonstration purposes
    ...     'decimalLongitude': [149.125, 149.133],
    ...     'date': ["14-01-2023", "15-01-2023"],
    ...     'individualCount': [0, 2],
    ...     'scientificName': ["Callocephalon fimbriatum", "Eolophus roseicapilla"],
    ...     'country': ["AU", "AU"],
    ...     'occurrenceStatus': ["present", "present"],
    ... })
    >>> corella.check_dataset(occurrences=df)

.. program-output:: python corella_user_guide/checking_dataset_code.py 3 


Users have options
---------------------
``corella`` offers two options for checking a dataset, which we have detailed above: 
Running individual checks through ``set_`` functions, or running a “test suite” with 
``check_dataset()``. We hope that these alternative options provide users with different 
options for their workflow, allowing them to choose their favourite method or switch 
between methods as they standardise their data.