import corella
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.use_occurrences()
    assert "Please provide a dataframe" in str(e_info.value)

def test_use_occurrences_no_arguments():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    with pytest.raises(Exception) as e_info:
        corella.use_occurrences(dataframe=df)
    assert "No Darwin Core" in str(e_info.value)

def test_use_occurrences_occurrenceID_rename():
    df = pd.DataFrame({'id': ['1','2']})
    new_df = corella.use_occurrences(dataframe=df,occurrenceID='id')
    print(new_df)
    assert 'occurrenceID' in new_df.columns

def test_use_occurrences_catalogNumber_rename():
    df = pd.DataFrame({'id': ['1','2']})
    new_df = corella.use_occurrences(dataframe=df,catalogNumber='id')
    assert 'catalogNumber' in new_df.columns

def test_use_occurrences_recordNumber_rename():
    df = pd.DataFrame({'id': ['1','2']})
    new_df = corella.use_occurrences(dataframe=df,recordNumber='id')
    assert 'recordNumber' in new_df.columns

def test_use_occurrences_occurrenceID_rename():
    df = pd.DataFrame({'bor': ['HumanObservation','HumanObservation']})
    new_df = corella.use_occurrences(dataframe=df,basisOfRecord='bor')
    assert 'basisOfRecord' in new_df.columns

def test_use_occurrences_occurrenceStatus_rename():
    df = pd.DataFrame({'status': ['PRESENT','PRESENT']})
    new_df = corella.use_occurrences(dataframe=df,occurrenceStatus='status')
    assert 'occurrenceStatus' in new_df.columns

def test_use_occurrences_add_occurrenceIDs():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0]})
    new_df = corella.use_occurrences(dataframe=df,occurrenceID=True)
    assert 'occurrenceID' in new_df.columns

def test_use_occurrences_basisOfRecord_value_incorrect():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'basisOfRecord': ['observation','observation']})
    with pytest.raises(Exception) as e_info:
        corella.use_occurrences(dataframe=df)
    assert 'basisOfRecord' in str(e_info.value)

def test_use_occurrences_basisOfRecord_value_incorrect_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'bor': ['observation','observation']})
    with pytest.raises(Exception) as e_info:
        corella.use_occurrences(dataframe=df,basisOfRecord='bor')
    assert 'basisOfRecord' in str(e_info.value)

def test_use_occurrences_occurrenceIDs_value_duplicate():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'occurrenceID': ['1','1']})
    with pytest.raises(Exception) as e_info:
        corella.use_occurrences(dataframe=df)
    assert 'occurrenceID' in str(e_info.value)

def test_use_occurrences_occurrenceIDs_value_duplicate_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'id': ['1','1']})
    with pytest.raises(Exception) as e_info:
        corella.use_occurrences(dataframe=df,occurrenceID='id')
    assert 'occurrenceID' in str(e_info.value)

def test_use_occurrences_occurrenceStatus_wrong_value():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'occurrenceStatus': ['1','1']})
    with pytest.raises(Exception) as e_info:
        corella.use_occurrences(dataframe=df)
    assert 'occurrenceStatus' in str(e_info.value)

def test_use_occurrences_occurrenceStatus__wrong_value_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'status': ['1','1']})
    with pytest.raises(Exception) as e_info:
        corella.use_occurrences(dataframe=df,occurrenceStatus='status')
    assert 'occurrenceStatus' in str(e_info.value)