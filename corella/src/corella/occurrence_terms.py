import pandas as pd

def occurrence_terms():

    terms_versions_raw = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/refs/heads/master/vocabulary/term_versions.csv")
    terms_use = terms_versions_raw[terms_versions_raw['status'] == 'recommended']
    terms_use = terms_use.drop_duplicates(subset='term_localName')
    terms_use = terms_use.dropna(subset=['organized_in'])
    # terms_use = terms_use[~terms_use['organized_in'].str.contains('UseWithIRI')]
    return terms_use