import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'#Cria arquivo
DB_FILE = ROOT_DIR/ DB_NAME#diz o caminho que o aruivo tá fazendo
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT'
    'peso REAL'
    ')'
)

connection.commit()

cursor.close()
connection.close()