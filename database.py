# database.py

import sqlite3
import os

def create_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect('data/compta.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS factures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            type TEXT,
            montant REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_facture(date, description, type_, montant):
    conn = sqlite3.connect('data/compta.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO factures (date, description, type, montant)
        VALUES (?, ?, ?, ?)
    ''', (date, description, type_, montant))
    conn.commit()
    conn.close()
