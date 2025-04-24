# compta_logic.py

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def get_data():
    conn = sqlite3.connect('data/compta.db')
    df = pd.read_sql_query("SELECT * FROM factures", conn)
    conn.close()
    df['date'] = pd.to_datetime(df['date'])
    return df

def bilan(df):
    total_revenu = df[df['type'] == 'revenu']['montant'].sum()
    total_depense = df[df['type'] == 'depense']['montant'].sum()
    solde = total_revenu - total_depense
    return total_revenu, total_depense, solde

def plot_pie(df):
    revenu, depense, _ = bilan(df)
    plt.figure(figsize=(5, 5))
    plt.pie([revenu, depense], labels=['Revenus', 'Dépenses'], autopct='%1.1f%%', colors=['green', 'red'])
    plt.title('Répartition des revenus/dépenses')
    plt.show()
