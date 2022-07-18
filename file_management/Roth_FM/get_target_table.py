import pandas as pd
def get_target_table(subjectID, folderPath):
    Target_Table = pd.read_csv(folderPath + subjectID + 'Target_Table.csv' )
    return Target_Table
