import mysql.connector
from restaurant_parse import get_all_restaurants


try:
    db = mysql.connector.connect(
        host='localhost',
        database='test_db',
        user='root',
        password=''
    )

    cursor = db.cursor()

    restaurants = get_all_restaurants()

    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS restaurants (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                link_site VARCHAR(30),
                category VARCHAR(255),
                rating VARCHAR(255),
                extras VARCHAR(511)
            )
        '''
    )

    for res in restaurants:
        cursor.execute(
            '''
                INSERT INTO restaurants(title, link_site, category, rating, extras)
                VALUES(%s, %s, %s, %s, %s)
            ''',
            (res['Title'], res['Link to website'], res['Category'], res['Rating'], str(res['Extras']))
        )
    db.commit()

    cursor.execute('SELECT * FROM restaurants')
    db_restaurants = cursor.fetchall()
    print(db_restaurants)

except Exception as e:
    print(e)
finally:
    if db.is_connected():
        cursor.close()
        db.close()
