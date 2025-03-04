import os
import os.path

def get_most_recent_file(path, key_string = "", dateformat = "MM_DD_YYYY"):
    """
    key_string can be a single string or a list of strings
    dateformat : {"MM_DD_YYYY", "DD_MM_YYYY"}
    assumes file is a .pkl"""
    if dateformat not in ["MM_DD_YYYY", "DD_MM_YYYY"]:
        raise ValueError("Improper date format. Set dateformat to either \"MM_DD_YYYY\" or \"DD_MM_YYYY\"")
        
    for (dirpath, dirnames, filenames) in os.walk(path):
        most_recent_file = ""
        most_recent_date = {"MM": 0, "YYYY": 0, "DD": 0}
        file_components = {"prefix": "", "date": "", "extension" : ""}
       
        key_string_flag = 0
        date_flag = 0
        file_found_flag = 0
        #for every file
        for i, filename in enumerate(filenames):
            #check if key_string is in the filename and that the filename ends with the year
            if isinstance(key_string, list):
                for key in key_string:
                    if key not in filename:
                        key_string_flag = 0
                        break
                    key_string_flag = 1
            else:
                if key_string in filename:
                    key_string_flag = 1
                else:
                    key_string_flag = 0
                    
            if key_string_flag:
                prefix, extension = os.path.splitext(filename)
                file_components["prefix"] = prefix[:-10]
                file_components["extension"] = extension
                file_components["date"] = prefix[-10:]
                
                if file_components["date"][-4:].isnumeric():
                    date_flag = 1
                    file_found_flag = 1
                    #temp dat/time variables
                    year  = file_components["date"][-4:]
                    if dateformat == "MM_DD_YYYY":
                        day     = file_components["date"][3:5]
                        month   = file_components["date"][0:2]
                    else:
                        month = file_components["date"][3:5]
                        day   = file_components["date"][0:2]
                       
                    #Check if this file is more recent than the previous file
                    if int(year) >= int(most_recent_date["YYYY"]):
                        most_recent_date["YYYY"] = year
                        most_recent_file = "".join(file_components.values())
                        if int(month) >= int(most_recent_date["MM"]):
                            most_recent_date["MM"] = month
                            most_recent_file = "".join(file_components.values())
                            if int(day) >= int(most_recent_date["DD"]):
                                most_recent_date["DD"] = day
                                most_recent_file = "".join(file_components.values())

                
        if not key_string_flag and not file_found_flag: raise FileNotFoundError(f"No file with key_string \"{key_string}\" exists.")
        if not date_flag and not file_found_flag: raise FileNotFoundError("No file with properly formatted date found.")
         
        return most_recent_file