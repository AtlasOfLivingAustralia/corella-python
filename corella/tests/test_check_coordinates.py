import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_coordinates()
    assert "Please provide a dataframe" in str(e_info.value)

def test_decimalLatitude_not_float():
    df = pd.DataFrame({'decimalLatitude': ['-1.0','-1.0']})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_decimalLongitude_not_float():
    df = pd.DataFrame({'decimalLongitude': ['-1.0','-1.0']})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_coordinatePrecision_not_float():
    df = pd.DataFrame({'coordinatePrecision': ['-1.0','-1.0']})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_coordinateUncertaintyInMeters_not_numeric():
    df = pd.DataFrame({'coordinateUncertaintyInMeters': ['-1.0','-1.0']})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_geodeticDatum_not_float():
    df = pd.DataFrame({'geodeticDatum': [1.0,1.0]})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_decimalLatitude_not_in_range():
    df = pd.DataFrame({'decimalLatitude': [-91.0,91.0]})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_decimalLongitude_not_in_range():
    df = pd.DataFrame({'decimalLongitude': [-181.0,181.0]})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_decimalLongitude_decimalLatitude_not_float():
    df = pd.DataFrame({'decimalLongitude': ['-1.0','-1.0'],'decimalLatitude': ['-1.0','-1.0']})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 2

def test_coordinatePrecision_not_in_range():
    df = pd.DataFrame({'coordinatePrecision': [-1.0,-1.0]})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_coordinatePrecision_coordinateUncertaintyInMeters_not_in_range():
    df = pd.DataFrame({'coordinatePrecision': [-1.0,-1.0],'coordinateUncertaintyInMeters': [-1.0,-1.0]})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 2

def test_coordinateUncertaintyInMeters_not_in_range():
    df = pd.DataFrame({'coordinateUncertaintyInMeters': [-1.0,-1.0]})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 1

def test_decimalLongitude_decimalLatitdue_coordinateUncertaintyInMeters_not_numeric():
    df = pd.DataFrame({'decimalLongitude': ['-1.0','-1.0'],
                       'decimalLatitude': ['-1.0','-1.0'],
                       'coordinateUncertaintyInMeters': ['-1.0','-1.0']})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 3

def test_decimalLongitude_decimalLatitdue_coordinateUncertaintyInMeters_geodeticDatum_incorrect():
    df = pd.DataFrame({'decimalLongitude': ['-1.0','-1.0'],
                       'decimalLatitude': ['-1.0','-1.0'],
                       'coordinateUncertaintyInMeters': ['-1.0','-1.0'],
                       'geodeticDatum': [1.0,1.0]})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 4

def test_decimalLongitude_decimalLatitdue_coordinateUncertaintyInMeters_geodeticDatum_coordinatePrecision_incorrect():
    df = pd.DataFrame({'decimalLongitude': ['-1.0','-1.0'],
                       'decimalLatitude': ['-1.0','-1.0'],
                       'coordinateUncertaintyInMeters': ['-1.0','-1.0'],
                       'geodeticDatum': [1.0,1.0],
                       'coordinatePrecision': ['-1.0','-1.0']})
    errors = corella.check_coordinates(dataframe=df)
    assert len(errors) == 5