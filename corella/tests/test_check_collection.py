import corella
import pytest
import pandas as pd
import uuid

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_collection()
    assert "Please provide a dataframe" in str(e_info.value)

def test_datasetName_not_string():
    df = pd.DataFrame({'datasetName': [1,1]})
    errors = corella.check_collection(dataframe=df,errors=[])
    assert len(errors) == 1

def test_datasetName_string_catalogNumber_not_string():
    df = pd.DataFrame({'datasetName': ['test','test'], 'catalogNumber': [1,1]})
    errors = corella.check_collection(dataframe=df,errors=[])
    assert len(errors) == 1

def test_datasetName_datasetID_string_catalogNumber_not_string():
    df = pd.DataFrame({'datasetName': ['test','test'], 'catalogNumber': [1,1], 'datasetID': "testing"})
    errors = corella.check_collection(dataframe=df,errors=[])
    assert len(errors) == 1

def test_datasetID_uuid():
    df = pd.DataFrame({'datasetID': [uuid.uuid4()]})
    errors = corella.check_collection(dataframe=df,errors=[])
    assert len(errors) == 0

def test_datasetName_string_datasetID_catalogNumber_not_string():
    df = pd.DataFrame({'datasetName': ['test','test'], 'catalogNumber': [1,1], 'datasetID': [1,1]})
    errors = corella.check_collection(dataframe=df,errors=[])
    assert len(errors) == 2

def test_datasetName_datasetID_catalogNumber_not_string():
    df = pd.DataFrame({'datasetName': [1,1], 'catalogNumber': [1,1], 'datasetID': [1,1]})
    errors = corella.check_collection(dataframe=df,errors=[])
    assert len(errors) == 3
#'''