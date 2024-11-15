import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_basisOfRecord()
    assert "Please provide a dataframe" in str(e_info.value)

def test_wrong_column_value():
    df = pd.DataFrame({'basisOfRecord': ['human','human']})
    errors = corella.check_basisOfRecord(dataframe=df,errors=[])
    assert len(errors) == 1

def test_correct_column_value():
    df = pd.DataFrame({'basisOfRecord': ['HumanObservation','HumanObservation']})
    new_df = corella.check_basisOfRecord(dataframe=df,errors=[])
    print(new_df)
    assert type(new_df) is pd.DataFrame