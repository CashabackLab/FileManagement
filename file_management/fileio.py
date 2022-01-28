import os
import os.path

def normalize_path(path):
  """Normalizes path variables for your OS"""
  return os.path.normpath(path)

def get_most_recent_file(path, key_string = "loss"):
    """File names must end with date formated as DD_MM_YYYY"""
    for (dirpath, dirnames, filenames) in os.walk(path):
        most_recent_year  = "0000"
        most_recent_month = "0"
        most_recent_day   = "0"
        most_recent_time = -1 #used if two files have the same date, will return most recent file by edit date
        most_recent_file = ""
        
        #for every file
        for filename in filenames:
            #check if key_string is in the filename and that the filename ends with the year
            if key_string in filename and filename[-8:-4].isnumeric():
                #temp dat/time variables
                year  = filename[-8:-4]
                month = filename[-11:-9]
                day   = filename[-14:-12]
                time   = os.path.getctime(os.path.join(path, filename))
                
                #Check if this file is more recent than the previous file
                if int(year) >= int(most_recent_year):
                    most_recent_year = year
                    if int(month) >= int(most_recent_month):
                        most_recent_month = month
                        if int(day) >= int(most_recent_day):
                            most_recent_day = day
                            if time > most_recent_time:
                                most_recent_time = time
                                most_recent_file = filename
        
        return most_recent_file
