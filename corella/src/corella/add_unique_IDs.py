import uuid
from .common_functions import check_for_dataframe

def add_unique_IDs(dataframe=None,
                   column_name="occurrenceID",
                   column_info=None,
                   sep='-'):
        """
        Function that automatically adds unique IDs (in the form of uuids) to each of your occurrences.

        Parameters
        ----------
            dataframe : ``pandas Dataframe``
                ``dataframe`` containing your data.
            column_name : ``str``
                String containing name of column you want to add.  Default is ``occurrenceID``
            column_info: ``str``, ``logical`` or ``list``
              Contains column names for 
            sep: ``char``
                Separation character for composite IDs.  Default is ``-``.

        Returns
        -------
            ``None``

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("occurrences_dwc.csv")
            data = corella.add_unique_IDs()
            data

        .. program-output:: python -c "import galaxias;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.add_unique_occurrence_IDs();print(my_dwca.occurrences)"
        """
        # check for empty dataframe
        check_for_dataframe(dataframe=dataframe,func='add_unique_IDs')

        # declare valid ID column names
        valid_id_names = ["occurrenceID","catalogNumber","recordNumber","eventID"]

        print(column_info)
        
        # check if column name is in valid_id_names; if it is, add column.  If not, raise ValueError.
        if column_name in valid_id_names:
            if type(column_info) is bool and column_info:
                return generate_uuids(dataframe=dataframe,column_name=column_name)
            elif type(column_info) is str:
                if column_info == 'random':
                    return generate_uuids(dataframe=dataframe,column_name=column_name)
                elif column_info == 'sequential':
                    ids = [str(x) for x in range(dataframe.shape[0])]
                    dataframe.insert(0,column_name,ids)
                    return dataframe
                else:
                    raise ValueError("Please provide either a valid column name, the word 'random' or the word 'sequential'.")
            elif type(column_info) is list:
                comp_id_info = []
                for ci in column_info:
                    if ci in dataframe.columns:
                        comp_id_info += dataframe[ci]
                    elif ci == 'random':
                        comp_id_info += generate_uuids_list(dataframe=dataframe)
                    elif ci == 'sequential':
                        comp_id_info += [str(x) for x in range(dataframe.shape[0])]
                    else:
                        raise ValueError("Please provide either a valid column name, the word 'random' or the word 'sequential'.")
                dataframe.insert(0,column_name,comp_id_info)
                return dataframe 
        else:
            raise ValueError("Please provide one of the following column names: \n\n{}".format(valid_id_names))
        
def generate_uuids(dataframe=None,column_name=None):
    uuids = [None for i in range(dataframe.shape[0])]
    for i in range(dataframe.shape[0]):
        uuids[i] = str(uuid.uuid4())
    dataframe.insert(0,column_name,uuids)
    return dataframe

def generate_uuids_list(dataframe=None):
    uuids = [None for i in range(dataframe.shape[0])]
    for i in range(dataframe.shape[0]):
        uuids[i] = str(uuid.uuid4())
    return uuids