import psycopg2
import psycopg2.extras #For DictCursor
hostname = 'localhost'
database = 'Ds'  
username = 'postgres'
pwd = '1234'
port_id = 5432
try:
    # Using context manager for connection
    with psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    ) as conn:
        # Use context manager for cursor, with DictCursor
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # Drop table if it exists
            cur.execute('DROP TABLE IF EXISTS Ds')
            # Creating table
            create_script = '''CREATE TABLE IF NOT EXISTS Ds (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                Marks INT,
                Student_id VARCHAR(100)
            )'''
            cur.execute(create_script)
            # Insert data
            insert_script = '''INSERT INTO Ds (id, name, Marks, Student_id) VALUES (%s, %s, %s, %s)'''
            insert_values = [
                (1, 'Kavya', 50, 'abc'),
                (2, 'Vedika', 60, 'efg'),
                (3, 'Palak', 55, 'xyz')
            ]
            for record in insert_values:
                cur.execute(insert_script, record)
            # Show Initial Data
            cur.execute('SELECT * FROM Ds')
            rows = cur.fetchall()
            print("Initial data:")
            for row in rows:
                print(dict(row))   #
            # Updating data
            update_script = 'UPDATE Ds SET Marks = 80 WHERE id = 1'
            cur.execute(update_script)
            # Show after update
            cur.execute('SELECT * FROM Ds')
            rows = cur.fetchall()
            print("After update:")
            for row in rows:
                print(dict(row))
            # Delete data
            delete_script = 'DELETE FROM Ds WHERE id = 2'
            cur.execute(delete_script)
            #After delete
            cur.execute('SELECT * FROM Ds')
            rows = cur.fetchall()
            print("After delete:")
            for row in rows:
                print(dict(row))
            conn.commit()
except Exception as error:
    print("An error occurred:", error)
