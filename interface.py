# interface.py

import tkinter as tk
from database import insert_facture
from compta_logic import get_data, plot_pie
from export import export_excel

def launch_app():
    def submit():
        try:
            insert_facture(
                entry_date.get(),
                entry_desc.get(),
                var_type.get(),
                float(entry_montant.get())
            )
            result_label.config(text="✅ Facture ajoutée !", fg="green")
        except Exception as e:
            result_label.config(text=f"❌ Erreur : {e}", fg="red")

    window = tk.Tk()
    window.title("Saisie des factures")
    window.geometry("300x400")  # Taille de fenêtre plus lisible

    # Champs de saisie
    tk.Label(window, text="📅 Date (YYYY-MM-DD)").pack()
    entry_date = tk.Entry(window)
    entry_date
