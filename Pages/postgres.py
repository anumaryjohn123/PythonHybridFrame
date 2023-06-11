import psycopg2


def postgresql(self):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="Employee_details",
        user="postgres"
    )
    cursor = conn.cursor()
    return cursor


