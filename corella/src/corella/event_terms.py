import pandas as pd
import numpy as np

def event_terms():
    """
    do this later
    """
    terms_versions_raw = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/refs/heads/master/vocabulary/term_versions.csv")
    terms_use_first = terms_versions_raw[(terms_versions_raw['status'] == 'recommended') & (terms_versions_raw['rdf_type'].str.contains('Property'))]
    organizedin = terms_use_first['organized_in'].copy()
    organizedin = organizedin.replace({'http://purl.org/dc/elements/1.1/': 'http://purl.org/dc/elements/Generic',
                                        np.nan: 'http://purl.org/dc/elements/Generic',
                                        'http://purl.org/dc/terms/': 'http://purl.org/dc/elements/Generic'})
    terms_use_first = terms_use_first.drop(columns=['organized_in'],axis=1)  # try this
    terms_use_first = pd.concat([terms_use_first,organizedin],axis=1)
    terms_use_first = terms_use_first.drop_duplicates(subset='term_localName')
    terms_use_first = terms_use_first[~terms_use_first['organized_in'].str.contains('UseWithIRI')]
    terms_use_second = terms_use_first[terms_use_first['organized_in'].isin(['http://purl.org/dc/elements/Generic','http://rs.tdwg.org/dwc/terms/Event','http://purl.org/dc/terms/Location'])].reset_index(drop=True)
    return terms_use_second['term_localName']