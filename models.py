
from database import create_connection

def add_flavor(name, description, season, availability):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO flavors (name, description, season, availability) VALUES (?, ?, ?, ?)', 
                   (name, description, season, availability))
    conn.commit()
    conn.close()
