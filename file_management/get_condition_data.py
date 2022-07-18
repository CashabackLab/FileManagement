import pandas as pd
import os, fnmatch, re

def get_condition_data(subjectID, folderPath, experiment_name, TP_row = 1, num_trials = 200, only_events = False):
    """
    Loads participant data. returns a list of pandas dataframes. Each dataframe is one trial.
    If only_events = True, only loads event codes.
    """
    for file in os.listdir(folderPath):
        if fnmatch.fnmatch(file, f"{experiment_name}_{subjectID}_C*_TP{TP_row}_*.csv" ):
            block = re.search(f"{experiment_name}_{subjectID}_C(.*)_TP{TP_row}_(.*).csv", file).group(1)
            
            if only_events:
                data_files = [pd.read_csv(folderPath + f"{experiment_name}_{subjectID}_C{block}_TP{TP_row}_T{i}.csv").dropna() for i in range(1, num_trials+1)]
            else:
                data_files = [pd.read_csv(folderPath + f"{experiment_name}_{subjectID}_C{block}_TP{TP_row}_T{i}.csv") for i in range(1, num_trials+1)]
                
            return data_files
