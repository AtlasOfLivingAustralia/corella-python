from .common_functions import check_for_dataframe,set_data_workflow
from .check_individual_traits import check_individual_traits
import uuid

def set_individual_traits(dataframe=None,
                          individualID=None,
                          lifeStage=None,
                          sex=None,
                          vitality=None,
                          reproductiveCondition=None):

    check_for_dataframe(dataframe=dataframe,func='set_individual_traits')

    # column renaming dictionary
    mapping = {
        'individualID': individualID,
        'lifeStage': lifeStage,
        'sex': sex,
        'vitality': vitality,
        'reproductiveCondition': reproductiveCondition,
    }

    # denote accepted formats
    accepted_formats = {
        'individualID': [uuid.UUID,str,list],
        'lifeStage': [str,list],
        'sex': [str,list],
        'vitality': [str,list],
        'reproductiveCondition': [str,list],
    }

    # manually set values for function
    variables = [individualID,lifeStage,sex,vitality,reproductiveCondition]
    values = ['individualID','lifeStage','sex','vitality','reproductiveCondition']

    dataframe = set_data_workflow(func='set_individual_traits',dataframe=dataframe,mapping=mapping,variables=variables,
                                  values=values,accepted_formats=accepted_formats)
    
    errors = check_individual_traits(dataframe=dataframe,errors=[])

    # return errors if there are any; otherwise, return dataframe
    if len(errors) > 0:
        raise ValueError("There are some errors in your data.  They are as follows:\n\n{}".format('\n'.join(errors)))
    return dataframe