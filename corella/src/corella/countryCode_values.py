import pandas as pd

def countryCode_values():
    
    ccs = pd.read_csv('wikipedia_country_codes.csv')
    return ccs['Code']