import corella
import pytest
import datetime
import pandas as pd

def test_check_datetime_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_datetime()
    assert "Please provide a dataframe" in str(e_info.value)

def test_check_datetime_no_eventDate():
    df = pd.DataFrame({'date': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)]})
    errors = corella.check_datetime(df)
    assert len(errors) == 1

def test_eventDate_not_datetime():
    df = pd.DataFrame({'eventDate': ['1990/10/10','1990/10/10']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1

def test_year_not_int():
    df = pd.DataFrame({'eventDate': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)], 'year': ['1990','1990']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1

def test_month_not_int():
    df = pd.DataFrame({'eventDate': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)], 'month': ['10','10']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1

def test_day_not_int():
    df = pd.DataFrame({'eventDate': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)], 'day': ['10','10']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1

def test_eventTime_not_datetime():
    df = pd.DataFrame({'eventDate': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)], 'eventTime': ['0:00','0:00']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1

def test_eventDate_year_not_correct_format():
    df = pd.DataFrame({'eventDate': ['1990/10/10','1990/10/10'], 'year': ['1990','1990']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 2

def test_eventDate_year_month_not_correct_format():
    df = pd.DataFrame({'eventDate': ['1990/10/10','1990/10/10'], 'year': ['1990','1990'], 'month': ['10','10']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 3

def test_eventDate_year_month_day_not_correct_format():
    df = pd.DataFrame({'eventDate': ['1990/10/10','1990/10/10'], 'year': ['1990','1990'], 'month': ['10','10'],'day': ['10','10']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 4

def test_eventDate_year_month_day_eventTime_not_correct_format():
    df = pd.DataFrame({'eventDate': ['1990/10/10','1990/10/10'], 'year': ['1990','1990'], 'month': ['10','10'],'day': ['10','10'], 'eventTime': ['0:00','0:00']})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 5

def test_eventDate_out_of_range():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2025,10,10),datetime.datetime(2025,10,10)]})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1

def test_year_out_of_range():
    df = pd.DataFrame({'year': [2100,2100], 'eventDate': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)]})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1

def test_month_out_of_range():
    df = pd.DataFrame({'month': [13,13], 'eventDate': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)]})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1

def test_day_out_of_range():
    df = pd.DataFrame({'month': [66,66], 'eventDate': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)]})
    errors = corella.check_datetime(dataframe=df,errors=[])
    assert len(errors) == 1