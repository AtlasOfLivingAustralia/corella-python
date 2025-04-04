import pandas as pd

def event_terms():

    terms_versions_raw = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/refs/heads/master/vocabulary/term_versions.csv")
    terms_use_first = terms_versions_raw[terms_versions_raw['status'] == 'recommended']
    terms_use_second = terms_use_first[terms_use_first['organized_in'].isin(['Generic','Event','Location'])]
    return list(set(terms_use_second['term_localName']))