import mysql.connector
"""
Module for accessing to mysql database
Download XAMPP MySQL to work with
"""

try:
    db = mysql.connector.connect(
        host='localhost',
        database='test_db',
        user='root',
        password=''
    )

    # object which is used to control Database
    # we can do prepare queries by that
    cursor = db.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255)
        )
        '''
    )

    # cursor.execute(
    #     '''
    #     INSERT INTO users (username, email, password)
    #     VALUES('Smit', 'smit@gmail.com', 'test2321')
    #     '''
    # )
    # db.commit()

    cursor.execute(
        '''
        SELECT * FROM users
        '''
    ) # finding all
    users = cursor.fetchall()  # get results info as list
    print(users)

    # cursor.execute(
    #     '''
    #     DELETE FROM users WHERE id = %s
    #     ''', (1,)
    # )
    # db.commit()

except Exception as e:
    print(e.args)
finally:
    # getting closed every object
    if db.is_connected:
        cursor.close()
        db.close()
