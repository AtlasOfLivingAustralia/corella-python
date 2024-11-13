import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_locality()
    assert "Please provide a dataframe" in str(e_info.value)

def test_continent_not_string():
    df = pd.DataFrame({'continent': [-1.0,-1.0]})
    errors = corella.check_locality(dataframe=df,errors=[])
    assert len(errors) == 1

def test_continent_not_valid():
    df = pd.DataFrame({'continent': ['Austlia','Austrlia']})
    errors = corella.check_locality(dataframe=df,errors=[])
    assert len(errors) == 1

def test_country_not_string():
    df = pd.DataFrame({'country': [-1.0,-1.0]})
    errors = corella.check_locality(dataframe=df,errors=[])
    assert len(errors) == 1

def test_country_not_valid():
    df = pd.DataFrame({'country': ['Austlia','Austrlia']})
    errors = corella.check_locality(dataframe=df,errors=[])
    assert len(errors) == 1

def test_countryCode_not_string():
    df = pd.DataFrame({'countryCode': [-1.0,-1.0]})
    errors = corella.check_locality(dataframe=df,errors=[])
    assert len(errors) == 1

def test_countryCode_not_valid():
    df = pd.DataFrame({'countryCode': ['Austlia','Austrlia']})
    errors = corella.check_locality(dataframe=df,errors=[])
    assert len(errors) == 1

def test_stateProvince_not_string():
    df = pd.DataFrame({'stateProvince': [-1.0,-1.0]})
    errors = corella.check_locality(dataframe=df,errors=[])
    assert len(errors) == 1

def test_stateProvince_not_string():
    df = pd.DataFrame({'locality': [-1.0,-1.0]})
    errors = corella.check_locality(dataframe=df,errors=[])
    assert len(errors) == 1