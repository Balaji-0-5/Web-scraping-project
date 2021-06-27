import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)

    conn.execute(" CREATE TABLE IF NOT EXISTS T_SHIRTS (NAME TEXT, BRAND TEXT, PRICE TEXT, DISCOUNT TEXT)")

    print("Table created successfully!")

    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)

    insert_sql = "INSERT INTO T_SHIRTS (NAME, BRAND, PRICE, DISCOUNT) VALUES (?, ?, ?, ?)"

    conn.execute(insert_sql, values)

    conn.commit()
    conn.close()

def get_product_info(dbname):
    conn = sqlite3.connect(dbname)

    cur = conn.cursor()

    cur.execute("SELECT * FROM T_SHIRTS")

    table_data = cur.fetchall()

    for record in table_data:
        print(record)
    conn.close()
