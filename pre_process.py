from grakn.client import *
import pandas as pd
import os

name_dir = {
    "SENTENCE" : int,
    "TEXT" : str,
    "LEMMA" : str,
    "POS" : str,
}

POS = {
        "DET" : "determiner",
        "ADJ" : "adjective",
       "NOUN" : "noun",
       "VERB" : "verb",
       "AUX" : "auxilliary-verb"
       }

def pre_process(direct = r"C:\Users\kunge\Downloads\AIEngineer\AIEngineer\gtc_AI.engineer_Projektbeschreibung\DEP_tables2"):
    '''processes all data inside tables inside a folder'''
    file_list = make_file_list(direct)
    help_list = []
    for i in file_list:
        table = open_table(i)
        help_list = help_list + table_to_garkn(table)
    return help_list

def make_file_list(direct, extension = ""):
    """makes a list of all files of a specific type in a directory"""
    file_list = []
    for root, folders, files in os.walk(direct):
        for file in files:
            path = os.path.join(root, file)
            if os.path.isfile(path) and (extension == "" or file[-len(extension):].lower() == extension):
                file_list.append(path)
    return file_list

def open_table(file_path):
    table = pd.read_excel(file_path, header = 7, dtype = name_dir)
    return table

def table_to_garkn(table):
    help_list = []
    # if it is important add it to the table
    for j in table.index:
        if table.loc[j,"POS"] in POS:
            return_str = ""
            return_str = "insert $" + str(table.loc[j,"LEMMA"]) + " isa " + str(POS[table.loc[j,"POS"]] + ";")
            help_list.append(return_str)
    return help_list
            # if table.loc[j,"DEP"] != "ROOT":
    #             #what is the index of the dependency?
    #             return_str = return_str + ", has dependency " + str(table.at[table.loc[j,"head_text"],"LEMMA"])
    #             print(return_str)
    