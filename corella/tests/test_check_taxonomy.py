import corella
import pytest
import pandas as pd

'''
    - ``kingdom``
    - ``taxonRank``
    - ``class``
    - ``order``
    - ``family``
    - ``genus``
    - ``specificEpithet``
    - ``vernacularName``
'''

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_taxonomy()
    assert "Please provide a dataframe" in str(e_info.value)

def test_kingdom_not_string():
    df = pd.DataFrame({'kingdom': [1,1]})
    errors = corella.check_taxonomy(dataframe=df,errors=[])
    assert len(errors) == 1

def test_kingdom_string_phylum_not_string():
    df = pd.DataFrame({'kingdom': ['Animalia','Animalia'], 'phylum': [1,1]})
    errors = corella.check_taxonomy(dataframe=df,errors=[])
    assert len(errors) == 1

def test_kingdom_phylum_string_class_not_string():
    df = pd.DataFrame({'kingdom': ['Animalia','Animalia'], 'phylum': ['Porifera','Porifera'], 'class': [1,1]})
    errors = corella.check_taxonomy(dataframe=df,errors=[])
    assert len(errors) == 1

def test_kingdom_phylum_string_class_not_string():
    df = pd.DataFrame({'kingdom': ['Animalia','Animalia'], 'phylum': [1,1], 'class': [1,1]})
    errors = corella.check_taxonomy(dataframe=df,errors=[])
    assert len(errors) == 2

def test_kingdom_phylum_string_class_not_string():
    df = pd.DataFrame({'kingdom': [1,1], 'phylum': [1,1], 'class': [1,1]})
    errors = corella.check_taxonomy(dataframe=df,errors=[])
    assert len(errors) == 3
#'''