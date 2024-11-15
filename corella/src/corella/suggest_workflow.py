from tabulate import tabulate
import pandas as pd
from .common_dictionaries import ID_REQUIRED_DWCA_TERMS,GEO_REQUIRED_DWCA_TERMS
from .get_dwc_noncompliant_terms import get_dwc_noncompliant_terms

# df = pd.DataFrame({'species': ["Callocephalon fimbriatum", "Eolophus roseicapilla"], 'latitude': [-35.310, "-35.273"], 'longitude': [149.125, 149.133], 'eventDate': ["14-01-2023", "15-01-2023"], 'status': ["present", "present"]})

def suggest_workflow(dataframe=None):
    """
    Suggests a workflow to ensure your data conforms with the pre-defined Darwin Core standard.

    Parameters
    ----------
        dataframe: ``pandas.DataFrame``
            The ``pandas.DataFrame`` that contains your data to check.

    Returns
    -------
        A printed report detailing presence or absence of required data.

    Examples
    --------
        Suggest a workflow for a small dataset

        .. prompt:: python

            import pandas as pd
            import corella
            df = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 'latitude': [-35.310, '-35.273'], 'longitude': [149.125, 149.133], 'eventDate': ['14-01-2023', '15-01-2023'], 'status': ['present', 'present']})
            corella.suggest_workflow(dataframe=df)
            
        .. program-output:: python -c "import pandas as pd;import corella;df = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 'latitude': [-35.310, '-35.273'], 'longitude': [149.125, 149.133], 'eventDate': ['14-01-2023', '15-01-2023'], 'status': ['present', 'present']});print(corella.suggest_workflow(dataframe=df))"
    """

    # set up dictionary for printing results
    required_terms = {
        "Type": ["Identifier (at least one)",
                 "Record type",
                 "Scientific name",
                 "Location",
                 "Date/Time"],
        "Matched term(s)": ['-','-','-','-','-'],
        "Missing term(s)": [' OR '.join(ID_REQUIRED_DWCA_TERMS["Australia"]),
                            'basisOfRecord',
                            'scientificName',
                            GEO_REQUIRED_DWCA_TERMS["Australia"],
                            'eventDate']
    }

    # get matching and nonmatching terms
    unmatched_dwc_terms = get_dwc_noncompliant_terms(dataframe=dataframe)
    matched_dwc_terms = list(filter(lambda x: x not in unmatched_dwc_terms, list(dataframe)))

    # set terms for looping over
    terms = [
        ID_REQUIRED_DWCA_TERMS["Australia"],
        'basisOfRecord',
        'scientificName',
        GEO_REQUIRED_DWCA_TERMS["Australia"],
        'eventDate'
    ]

    # loop over all terms to compile what the person has in the dataframe
    for i,t in enumerate(terms):
        if type(t) is list and i == 0:
            if any(map(lambda v: v in ID_REQUIRED_DWCA_TERMS["Australia"],list(dataframe.columns))):
                column_present = list(map(lambda v: v in ID_REQUIRED_DWCA_TERMS["Australia"],list(dataframe.columns)))
                true_indices = column_present.index(True)
                if type(true_indices) is list:
                    required_terms["Matched term(s)"][i] = ', '.join(list(dataframe.columns)[true_indices])
                else:
                    required_terms["Matched term(s)"][i] = list(dataframe.columns)[true_indices]
                required_terms["Missing term(s)"][i] = '-'
        elif type(t) is list and i == 3:
            location_names = []
            for name in GEO_REQUIRED_DWCA_TERMS["Australia"]:
                if name in dataframe.columns:
                    location_names.append(name)
                    required_terms["Missing term(s)"][i].remove(name)
            if len(location_names) == 0:
                location_names = ['-']
            if len(required_terms["Missing term(s)"][i]) == 0:
                required_terms["Missing term(s)"][i] = ['-']
            required_terms["Matched term(s)"][i] = ', '.join(location_names)
            required_terms["Missing term(s)"][i] = ', '.join(required_terms["Missing term(s)"][i])
        else:
            if t in list(dataframe.columns):
                required_terms["Matched term(s)"][i] = t
                required_terms["Missing term(s)"][i] = '-'

    # print results
    print("\n── Darwin Core terms ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("\n── All DwC terms ──")
    # change to include events, multimedia and emof
    print("\nMatched {} of {} column names to DwC terms:\n".format(len(matched_dwc_terms),len(dataframe.columns)))
    print("{} Matched: {}".format(u'\u2713',', '.join(matched_dwc_terms)))
    print("{} Unmatched: {}".format(u'\u2717',', '.join(unmatched_dwc_terms)))
    print("\n── Minimum required DwC terms ──\n")
    terms = pd.DataFrame(required_terms)
    print(tabulate(terms, showindex=False, headers=terms.columns))
    print("\n── Suggested workflow ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    if list(required_terms["Missing term(s)"]) == ['-','-','-','-','-']:
        print("\nCongratulations! You have the required Darwin Core terms. Use corella.check_occurrences() to check whether your data is also Darwin Core compliant.")
    else:
        print("To make your data Darwin Core compliant, use the following workflow:\n")
        if required_terms["Matched term(s)"][0] == '-' or required_terms["Matched term(s)"][1] == '-':
            print("corella.use_occurrences()")
        if required_terms["Matched term(s)"][2] == '-':
            print("corella.use_scientific_name()")
        if required_terms["Missing term(s)"][3] != '-':
            print("corella.use_coordinates()")
        if required_terms["Matched term(s)"][4] == '-':
            print("corella.use_datetime()")    
        print("\nAdditional functions: use_abundance(), use_locality()")