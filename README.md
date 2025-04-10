
<!-- README.md is generated from README.Rmd. Please edit that file -->

# corella <a href="https://corella.ala.org.au"><img src="docs/source/_static/logo/logo.png" align="right" height="139" alt="corella website" /></a>

<!-- badges: start -->

[![pypi](https://img.shields.io/pypi/v/galah-python.svg)](https://pypi.org/project/galah-python/)

<!-- badges: end -->

## Overview

`corella-python` is an R package that helps users standardize their data using
the [*Darwin Core*](https://dwc.tdwg.org) data standard, used for
biodiversity data like species occurrences. `corella-python` provides tools to
prepare, manipulate and validate data against the standard’s criteria.
Once standardized, data can be subsequently shared as a [*Darwin Core
Archive*](https://ipt.gbif.org/manual/en/ipt/latest/dwca-guide#what-is-darwin-core-archive-dwc-a)
and published to open data infrastructures like the [Atlas of Living
Australia](https://www.ala.org.au) and [GBIF](https://www.gbif.org/).

`corella-python` was built, and is maintained, by the [Science & Decision
Support Team](https://labs.ala.org.au) at the [Atlas of Living
Australia](https://www.ala.org.au) (ALA). It is named for the Little
Corella ([*Cacatua
sanguinea*](https://bie.ala.org.au/species/https%3A//biodiversity.org.au/afd/taxa/34b31e86-7ade-4cba-960f-82a6ae586206)).
The logo was designed by [Dax Kellie](https://daxkellie.com/).

If you have any comments, questions or suggestions, please [contact
us](mailto:support@ala.org.au).

## Installation

Install from PyPI:

``` bash
pip install corella-python
```

Install the development version of `corella-python` from GitHub:

``` bash
git clone https://github.com/AtlasOfLivingAustralia/corella-python.git
cd corella
pip install .
```

## Usage

Here we have a small sample of example data containing observations of
cockatoos. Using corella we can convert our data to use Darwin Core
Standard.

``` python
>>> import corella
>>> import pandas as pd

# A simple example of species occurrence data
>>> df = pd.DataFrame({
...     'species': ["Callocephalon fimbriatum", "Eolophus roseicapilla"],
...     'latitude': [-35.310, -35.273],
...     'longitude': [149.125, 149.133],
...     'eventDate': ["14-01-2023", "15-01-2023"],
...     'status': ["present", "present"]
... })
>>> df
                    species latitude  longitude   eventDate   status
0  Callocephalon fimbriatum   -35.31    149.125  14-01-2023  present
1     Eolophus roseicapilla  -35.273    149.133  15-01-2023  present
```

One of the most important aspects of Darwin Core Standard is using
standard column names (Darwin Core *terms*). We can update column names
in our data to match Darwin Core terms with `set_` functions.

Each `set_` function name corresponds to the type of data, and argument
names correspond to the available Darwin Core terms to use as column
names. `set_` functions support data wrangling operations &
`dplyr::mutate()` functionality, meaning columns can be changed or fixed
in your pipe. `set_` functions will indicate if anything needs fixing
because they also automatically run checks on each column data to make
sure each column is in the correct format.

``` python
>>> df = corella.set_coordinates(dataframe=df,
...                              decimalLatitude='latitude',
...                              decimalLongitude='longitude')
>>> df = corella.set_scientific_name(dataframe=df,scientificName='species')
>>> df = corella.set_datetime(dataframe=df,string_to_datetime=True,dayfirst=True)
>>> df = corella.set_occurrences(dataframe=df,occurrenceStatus='status')
>>> df
             scientificName  decimalLatitude  decimalLongitude  eventDate occurrenceStatus
0  Callocephalon fimbriatum          -35.310           149.125 2023-01-14          present
1     Eolophus roseicapilla          -35.273           149.133 2023-01-15          present
```

Not sure where to start? Use `suggest_workflow()` to know what steps you
need to make to make your data Darwin Core compliant.

``` python
>>> corella.suggest_workflow(occurrences=df)

── Darwin Core terms ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

── All DwC terms ──

Matched 1 of 5 column names to DwC terms:

✓ Matched: eventDate
✗ Unmatched: latitude, longitude, status, species

── Minimum required DwC terms occurrences ──

Type                       Matched term(s)    Missing term(s)
-------------------------  -----------------  ------------------------------------------------
Identifier (at least one)  -                  occurrenceID OR catalogNumber OR recordNumber
Record type                -                  basisOfRecord
Scientific name            -                  scientificName
Location                   -                  decimalLatitude, decimalLongitude, geodeticDatum
Date/Time                  eventDate          -

── Suggested workflow ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

── Occurrences ──

To make your occurrences Darwin Core compliant, use the following workflow:

corella.set_occurrences()
corella.set_scientific_name()
corella.set_coordinates()

Additional functions: set_abundance(), set_collection(), set_individual_traits(), set_license(), set_locality(), set_taxonomy()
```

Or, if your data is nearly ready and you want to run checks over all
columns that match Darwin Core terms, run `check_dataset()`.

``` python
>>> corella.check_dataset(occurrences=df)

  Number of Errors  Pass/Fail    Column name
------------------  -----------  -------------
                 1  ✗            eventDate


══ Results ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════


Errors: 1 | Passes: 0

✗ Data does not meet minimum Darwin core requirements
Use corella.suggest_workflow()

── Error in eventDate ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

the eventDate column must be in datetime format.
```

## Citing corella

The current recommended citation is:

> Buyan A & Westgate MJ (2025) corella: Tools to standardize biodiversity data to Darwin Core. Python package v0.1.0.
