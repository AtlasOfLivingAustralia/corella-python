import corella
import pytest
import pandas as pd
import uuid

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_individual_traits()
    assert "Please provide a dataframe" in str(e_info.value)

def test_individualID_not_correct_type():
    df = pd.DataFrame({'individualID': [1,1]})
    errors = corella.check_individual_traits(dataframe=df,errors=[])
    

def test_individualID_uuids():
    df = pd.DataFrame({'individualID': [uuid.uuid4(),uuid.uuid4()]})
    errors = corella.check_individual_traits(dataframe=df,errors=[])
    assert 'individualID' in df.columns

def test_lifeStage_not_string():
    df = pd.DataFrame({'lifeStage': [1,1]})
    errors = corella.check_individual_traits(dataframe=df,errors=[])
    assert len(errors) == 1

def test_lifeStage_sex_not_string():
    df = pd.DataFrame({'lifeStage': [1,1], 'sex': [1,1]})
    errors = corella.check_individual_traits(dataframe=df,errors=[])
    assert len(errors) == 2

def test_lifeStage_sex_vitality_not_string():
    df = pd.DataFrame({'lifeStage': [1,1], 'sex': [1,1],'vitality': [1,1]})
    errors = corella.check_individual_traits(dataframe=df,errors=[])
    assert len(errors) == 3

def test_lifeStage_sex_vitality_reproductiveCondition_not_string():
    df = pd.DataFrame({'lifeStage': [1,1], 'sex': [1,1],'vitality': [1,1], 'reproductiveCondition': [1,1]})
    errors = corella.check_individual_traits(dataframe=df,errors=[])
    assert len(errors) == 4

def test_lifeStage_sex_vitality_reproductiveCondition_string():
    df = pd.DataFrame({'lifeStage': ['1','1'], 'sex': ['1','1'],'vitality': ['1','1'], 'reproductiveCondition': ['1','1']})
    errors = corella.check_individual_traits(dataframe=df,errors=[])
    assert all(x in df.columns for x in ['lifeStage','sex','vitality','reproductiveCondition'])