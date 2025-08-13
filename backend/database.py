import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("MYSQL_HOST")
PORT = int(os.getenv("MYSQL_PORT", 3306))
USER = os.getenv("MYSQL_USER")
PASS = os.getenv("MYSQL_PASS")
DB = os.getenv("MYSQL_DB")

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASS,
            database=DB,
            autocommit=True
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"La base de datos {DB} no existe.")
        else:
            print(f"Error de conexión a MySQL: {err}")
        return None

def init_db():
    conn = get_connection()
    if not conn:
        print("Error conectando a la base de datos")
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    cursor.close()
    conn.close()

def save_contact(name: str, email: str, message: str):
    conn = get_connection()
    if not conn:
        print("Error conectando a la base de datos")
        return
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s);",
        (name, email, message)
    )
    cursor.close()
    conn.close()
