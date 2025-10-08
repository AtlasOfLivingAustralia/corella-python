:orphan:

.. _Installation:

Prerequisites
=================================

You will need the following packages to be able to run ``galah``:

- `pandas <https://pandas.pydata.org/>`_
- `beautifulsoup4 <https://beautiful-soup-4.readthedocs.io/en/latest/>`_
- `configparser <https://pypi.org/project/configparser/>`_
- `pytest <https://pypi.org/project/pytest/>`_
- `requests <https://requests.readthedocs.io/en/latest/>`_
- `shutils <https://pypi.org/project/shutils/>`_
- `tabulate <https://pypi.org/project/tabulate/>`_

To install all of these at once, run

.. prompt:: 

    pip install pandas beautifulsoup4 configparser pytest requests shutils tabulate

WARNING: If you're installing all of the packages in one go, make sure you check that the installation ran successfully.  If one package doesnt work, the rest following wont install...

Installation
=================================

Installation can be performed a number of ways: the Python Package Index (PyPI) or from the Github page. 

Python Package Index
--------------------

To install the latest version of ``corella`` using pip do:

.. prompt:: 

    pip install corella-python

To upgrade to the latest release:

.. prompt:: 

    pip install --upgrade corella-python

Source
------

Ensure that you have ``git`` installed, and then clone the repo:


.. prompt:: 

    git clone https://github.com/AtlasOfLivingAustralia/corella_python.git

Then go into the ``corella-python/corella`` directory and run the following command:

.. prompt:: 

    pip install .