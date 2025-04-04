import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_license()
    assert "Please provide a dataframe" in str(e_info.value)

def test_license_not_string():
    df = pd.DataFrame({'license': [-1.0,-1.0]})
    errors = corella.check_license(dataframe=df,errors=[])
    assert len(errors) == 1

def test_rightsHolder_not_string():
    df = pd.DataFrame({'rightsHolder': [-1.0,-1.0]})
    errors = corella.check_license(dataframe=df,errors=[])
    assert len(errors) == 1

def test_accessRights_not_string():
    df = pd.DataFrame({'accessRights': [-1.0,-1.0]})
    errors = corella.check_license(dataframe=df,errors=[])
    assert len(errors) == 1

def test_license_rightsHolder_not_string():
    df = pd.DataFrame({'license': [-1.0,-1.0],'rightsHolder': [-1.0,-1.0]})
    errors = corella.check_license(dataframe=df,errors=[])
    assert len(errors) == 2

def test_license_rightsHolder_accessRights_not_string():
    df = pd.DataFrame({'license': [-1.0,-1.0],'rightsHolder': [-1.0,-1.0],'accessRights': [-1.0,-1.0]})
    errors = corella.check_license(dataframe=df,errors=[])
    assert len(errors) == 3