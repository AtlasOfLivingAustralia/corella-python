import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_scientificName()
    assert "Please provide a dataframe" in str(e_info.value)

def test_scientificName_not_string():
    df = pd.DataFrame({'scientificName': [-1.0,-1.0]})
    errors = corella.check_scientificName(dataframe=df,errors=[])
    assert len(errors) == 1

def test_scientificNameRank_not_string():
    df = pd.DataFrame({'scientificNameRank': [-1.0,-1.0]})
    errors = corella.check_scientificName(dataframe=df,errors=[])
    assert len(errors) == 1

def test_scientificNameAuthorship_not_string():
    df = pd.DataFrame({'scientificNameAuthorship': [-1.0,-1.0]})
    errors = corella.check_scientificName(dataframe=df,errors=[])
    assert len(errors) == 1

def test_scientificName_scientificNameRank_not_string():
    df = pd.DataFrame({'scientificName': [-1.0,-1.0],'scientificNameRank': [-1.0,-1.0]})
    errors = corella.check_scientificName(dataframe=df,errors=[])
    assert len(errors) == 2

def test_scientificName_scientificNameRank_scientificNameAuthorship_not_string():
    df = pd.DataFrame({'scientificName': [-1.0,-1.0],'scientificNameRank': [-1.0,-1.0],'scientificNameAuthorship': [-1.0,-1.0]})
    errors = corella.check_scientificName(dataframe=df,errors=[])
    assert len(errors) == 3