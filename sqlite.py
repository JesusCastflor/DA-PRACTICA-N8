import sqlite3
conn = sqlite3.connect('pedidos.db')
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
            userid INT PRIMARY KEY,
            fname TEXT,
            lname TEXT,
            gender TEXT);
            """)
conn.commit()
cur.execute("""
            CREATE TABLE IF NOT EXISTS orders(
            orderid INT PRIMARY KEY,
            date TEXT,
            userid TEXT,
            total TEXT,
            FOREIGN KEY (userid) REFERENCES users(userid)
            );
            """)
conn.commit()