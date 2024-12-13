import uuid
from .common_functions import check_for_dataframe

def add_unique_IDs(column_name="occurrenceID",
                   dataframe=None):
        """
        Function that automatically adds unique IDs (in the form of uuids) to each of your occurrences.

        Parameters
        ----------
            ``column_name`` : ``str``
                String containing name of column you want to add.  Default is ``occurrenceID``
            ``dataframe`` : ``pandas Dataframe``
                ``dataframe`` containing your data.

        Returns
        -------
            ``None``

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("occurrences_dwc.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.add_unique_occurrence_IDs()
            my_dwca.occurrences

        .. program-output:: python -c "import galaxias;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.add_unique_occurrence_IDs();print(my_dwca.occurrences)"
        """
        # check for empty dataframe
        check_for_dataframe(dataframe=dataframe,func='add_unique_IDs')

        # declare valid ID column names
        valid_id_names = ["occurrenceID","catalogNumber","recordNumber","eventID"]
        
        # check if column name is in valid_id_names; if it is, add column.  If not, raise ValueError.
        if column_name in valid_id_names:
            uuids = [None for i in range(dataframe.shape[0])]
            for i in range(dataframe.shape[0]):
                uuids[i] = str(uuid.uuid4())
            dataframe.insert(0,column_name,uuids)
            return dataframe
        else:
            raise ValueError("Please provide one of the following column names: \n\n{}".format(valid_id_names))