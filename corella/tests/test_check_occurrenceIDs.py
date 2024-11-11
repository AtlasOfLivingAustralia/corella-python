import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_occurrenceIDs()
    assert "Please provide a dataframe" in str(e_info.value)

def test_occurrenceIDs_not_unique():
    df = pd.DataFrame({'occurrenceID': ['1.0','1.0']})
    errors = corella.check_occurrenceIDs(dataframe=df)
    assert len(errors) == 1

def test_catalogNumbers_not_unique():
    df = pd.DataFrame({'catalogNumber': ['1.0','1.0']})
    errors = corella.check_occurrenceIDs(dataframe=df)
    assert len(errors) == 1

def test_recordNumber_not_unique():
    df = pd.DataFrame({'recordNumber': ['1.0','1.0']})
    errors = corella.check_occurrenceIDs(dataframe=df)
    assert len(errors) == 1

def test_occurrenceIDs_catalogNumbers_not_unique():
    df = pd.DataFrame({'occurrenceID': ['1','1'], 'catalogNumber': [1,1]})
    errors = corella.check_occurrenceIDs(dataframe=df)
    assert len(errors) == 2

def test_occurrenceIDs_catalogNumbers_recordNumbers_not_unique():
    df = pd.DataFrame({'occurrenceID': ['1','1'], 'catalogNumber': [1,1], 'recordNumber': [2,2]})
    errors = corella.check_occurrenceIDs(dataframe=df)
    assert len(errors) == 3