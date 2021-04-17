import pandas as pd
import os

name_dir = {
    "SENTENCE" : int,
    "TEXT" : str,
    "LEMMA" : str,
    "POS" : str,
}

POS = {
        # "DET" : "determiner",
        "ADJ" : "adjective",
        "ADV" : "adjective",
       "NOUN" : "noun",
       "VERB" : "verb",
       "AUX" : "verb"
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

def open_table(file_path = r"C:\Users\kunge\Downloads\AIEngineer\AIEngineer\gtc_AI.engineer_Projektbeschreibung\DEP_tables2\elmot_0.xlsx"):
    table = pd.read_excel(file_path, header = 7, dtype = name_dir)
    return table

def table_to_garkn(table):
    help_list = []
    # if it is important add it to the table
    subject = []
    _object = []
    for j in table.index:
        if table.loc[j,"POS"] == "NOUN":
            help_list.append("insert $" + str(table.loc[j,"LEMMA"]) + " isa " + str(POS[table.loc[j,"POS"]]) + ", has text \"" +  str(table.loc[j,"LEMMA"] + "\";"))
        # check if more than 1 subject
            if "su" in table.loc[j,"DEP"]:
                subject.append(j)    
            else:
                _object.append(j)
    if len(subject) == 1:
        subject = subject[0]
        #for every object find the closest verb
        for obj in _object:
            distance = 100
            close_verb = 0
            for verb in table.index:
                if table.loc[verb,"POS"] == "VERB"  or table.loc[verb,"POS"] == "AUX":
                    if get_distance(subject, obj, verb) <= distance:
                        distance = get_distance(subject, obj, verb)
                        close_verb = verb
                        help_list.append("insert (subject: $"+ table.loc[subject,"LEMMA"] + ", " +"object: $"+ table.loc[obj,"LEMMA"]+ ") isa verb;")
    elif len(subject) == 0:
        print("No subject!")
    else: 
        print("{} subjects; not implemented yet!".format(len(subject)))            
    return help_list

def get_distance(sub, obj, verb):
    return abs(sub - verb) + abs(obj - verb) 