import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_abundance()
    assert "Please provide a dataframe" in str(e_info.value)

def test_individualCount_not_float():
    df = pd.DataFrame({'individualCount': ['1','1']})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 1

def test_occurrenceStatus_not_correct():
    df = pd.DataFrame({'individualCount': [1,0], 'occurrenceStatus': ['PRESENT','PRESENT']})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 1