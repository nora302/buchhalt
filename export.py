# export.py

from compta_logic import get_data
import pandas as pd

def export_excel():
    df = get_data()
    df.to_excel("export_compta.xlsx", index=False)
    print("Export Excel réussi !")
