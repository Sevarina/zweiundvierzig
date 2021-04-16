import pandas as pd

name_dir = {
    "SENTENCE" : int,
    "TEXT" : str,
    "LEMMA" : str,
    "POS" : str,
}

def open_table(file_path):
    table = pd.read_excel(file_path, header = 7,index_col = 1, dtype = name_dir)
    print(table)

open_table(r"C:\Users\kunge\Downloads\AIEngineer\AIEngineer\gtc_AI.engineer_Projektbeschreibung\DEP_tables2\elmot_0.xlsx")