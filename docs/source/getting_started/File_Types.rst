.. _File_Types:

What data does ``corella`` handle? 
=========================================

``corella`` has been built to handle most of the types of accepted Darwin Core files.  
For the "core" files, we can handle and check the following:

- ``occurrences.txt``: this is the file that contains your "occurrences," or sightings of species.  It contains information such as the scientific name of species, latitude and longitude, and date you observed the species.
- ``events.txt``: this file contains something called "events".  This describes activities like surveys and transects, and want to capture the biodiversity of a place over time.

It has also been adapted to handle and check the following extensions:

- ``multimedia.txt``: if you have images, videos or sounds, this is where you describe that kind of data
- ``extendedMeasurementOrFact.txt``: if you have data that captures the environment at the time of the observation, such as temperature, this is described in this file.