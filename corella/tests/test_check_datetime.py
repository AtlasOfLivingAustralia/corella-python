import corella
import pytest
import datetime
import pandas as pd

def test_check_datetime_no_dataframe():
    with pytest.raises(Exception) as e_info:
        corella.check_datetime()
    assert "Please provide a dataframe" in str(e_info.value)

# def test_check_datetime_no_eventDate():
#     df = pd.DataFrame({'date': [datetime.datetime(1990,10,10),datetime.datetime(1990,10,10)]})
#     with pytest.raises(Exception) as e_info:
#         corella.check_datetime(df)
#     assert "required field" in str(e_info.value)

# def test_check_datetime_no_dataframe():
#     with pytest.raises(Exception) as e_info:
#         corella.check_datetime()
#     assert "Please provide a dataframe" in str(e_info.value)

# def test_check_datetime_no_dataframe():
#     with pytest.raises(Exception) as e_info:
#         corella.check_datetime()
#     assert "Please provide a dataframe" in str(e_info.value)

# def test_check_datetime_no_dataframe():
#     with pytest.raises(Exception) as e_info:
#         corella.check_datetime()
#     assert "Please provide a dataframe" in str(e_info.value)

# def test_check_datetime_no_dataframe():
#     with pytest.raises(Exception) as e_info:
#         corella.check_datetime()
#     assert "Please provide a dataframe" in str(e_info.value)