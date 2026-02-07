import psycopg2

hostname = 'localhost'
database = 'Ds'
username = 'postgres'
pwd = '1234'
port_id = 5432

conn = None
cur = None
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    '''Return the data in form of  dictionary'''
    cur.execute('Drop the table if exists')
    create_script = '''CREATE TABLE IF NOT EXISTS Ds (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        Marks INT,
        Student_id VARCHAR(100)
    )'''
    cur.execute(create_script)

    insert_script = '''INSERT INTO Ds (id, name, Marks,Student_id) VALUES (%s, %s, %s, %s)'''
    insert_values = [
        (1, 'Kavya', 50, 'abc'),
        (2, 'Vedika', 60, 'efg'),
        (3, 'Palak', 55, 'xyz')
    ]
    '''Tuple '''
    for record in insert_values:
        cur.execute(insert_script, record)

    cur.execute('SELECT * FROM Ds')
    print(cur.fetchall())

    conn.commit()

except Exception as error:
    print("An error occurred:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
