import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_occurrenceStatus()
    assert "Please provide a dataframe" in str(e_info.value)

def test_check_occurrenceStatus_rename():
    df = pd.DataFrame({'occurrenceStatus': ['PRESENT','PRESENT']})
    new_df = corella.check_occurrenceStatus(dataframe=df)
    assert type(new_df) is pd.DataFrame

def test_check_occurrenceStatus_invalid_values():
    df = pd.DataFrame({'occurrenceStatus': ['here','here']})
    errors = corella.check_occurrenceStatus(dataframe=df)
    assert len(errors) == 1