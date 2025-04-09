import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_observer()
    assert "Please provide a dataframe" in str(e_info.value)

def test_recordedBy_not_string():
    df = pd.DataFrame({'recordedBy': [-1.0,-1.0]})
    errors = corella.check_observer(dataframe=df,errors=[])
    assert len(errors) == 1

def test_recordedByID_not_string():
    df = pd.DataFrame({'recordedByID': [-1.0,-1.0]})
    errors = corella.check_observer(dataframe=df,errors=[])
    assert len(errors) == 1

def test_recordedBy_recordedByID_not_string():
    df = pd.DataFrame({'recordedBy': [-1.0,-1.0],'recordedByID': [-1.0,-1.0]})
    errors = corella.check_observer(dataframe=df,errors=[])
    assert len(errors) == 2