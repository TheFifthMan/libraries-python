from contextlib import contextmanager
import pymysql

@contextmanager
def create_connection():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='qwe123',
                             db='apitesting',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        yield connection
    finally:
        connection.close()


with create_connection() as conn:
    with conn.cursor() as cursor:
        sql = "select * from account;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    conn.commit()