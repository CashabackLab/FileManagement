import pandas as pd

def get_trial_table(subjectID, folderPath):
    Trial_Table = pd.read_csv(folderPath + subjectID + 'Trial_Table.csv' )
    return Trial_Table
