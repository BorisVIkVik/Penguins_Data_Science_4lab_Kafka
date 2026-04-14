import psycopg2

conn =psycopg2.connect(
    dbname='penguinsDB',
    user='myuser',
    password='mypassword',
    host='localhost',
    port='5332'
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS predict_results_test (
        id SERIAL PRIMARY KEY,
        result VARCHAR(50)
    );
""")
conn.commit()

cur.execute(
    "INSERT INTO predict_results_test (result) VALUES (%s)",
    ("Krytoy penguins",)
)
conn.commit()

cur.execute("SELECT id, result FROM predict_results_test")
rows = cur.fetchall()
for r in rows:
    print(r)

cur.close()
conn.close()