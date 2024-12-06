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

def test_organismQuantity_not_correct_no_type():
    df = pd.DataFrame({'individualCount': [1,0], 'organismQuantity': [1,1]})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 1

def test_organismQuantity_no_type():
    df = pd.DataFrame({'individualCount': [1,0], 'organismQuantity': ['individual','individual']})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 2

def test_organismQuantityType_not_correct_no_type():
    df = pd.DataFrame({'individualCount': [1,0], 'organismQuantityType': [1,1]})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 2

def test_organismQuantityType_no_type():
    df = pd.DataFrame({'individualCount': [1,0], 'organismQuantityType': ['living individuals','living individuals']})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 1

def test_organismQuantity_organismQuantityType_wrong_var_types():
    df = pd.DataFrame({'individualCount': [1,0], 'organismQuantity': [1,0], 'organismQuantityType': [1,0]})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 1

def test_organismQuantity_organismQuantityType_wrong_var_type_orgQuantType():
    df = pd.DataFrame({'individualCount': [1,0], 'organismQuantity': ['individual','individual'], 'organismQuantityType': [1,0]})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 2

def test_organismQuantity_organismQuantityType_wrong_var_type_orgQuant():
    df = pd.DataFrame({'individualCount': [1,0], 'organismQuantity': [1,0], 'organismQuantityType': ['individual','individual']})
    errors = corella.check_abundance(dataframe=df,errors=[])
    assert len(errors) == 0
#'''