import mysql.connector
from dotenv import load_dotenv
import os
import pandas as pd  # <-- pandas para DataFrame

load_dotenv()

HOST = os.getenv("MYSQL_HOST")
PORT = int(os.getenv("MYSQL_PORT", 3306))
USER = os.getenv("MYSQL_USER")
PASS = os.getenv("MYSQL_PASS")
DB = os.getenv("MYSQL_DB")

def get_connection():
    return mysql.connector.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASS,
        database=DB
    )

def listar_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, message, created_at FROM contacts;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Definir nombres de columnas para el DataFrame
    columnas = ["ID", "Nombre", "Email", "Mensaje", "Fecha"]
    
    # Crear DataFrame y retornarlo
    df = pd.DataFrame(rows, columns=columnas)
    return df

if __name__ == "__main__":
    contacts_df = listar_contacts()
    if not contacts_df.empty:
        print(contacts_df)
    else:
        print("No hay contactos guardados.")
