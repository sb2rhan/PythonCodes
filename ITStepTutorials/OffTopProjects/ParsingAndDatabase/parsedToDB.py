import mysql.connector
import parserRestaurants


try:
    db = mysql.connector.connect(
        host='localhost',
        database='test_db',
        user='root',
        password=''
    )

    cursor = db.cursor()

    restaurants = parserRestaurants.get_all_restaurants()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS restaurants(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            link VARCHAR(255),
            phone_number VARCHAR(50),
            address VARCHAR(255),
            cuisine VARCHAR(255),
            cost VARCHAR(20),
            additional VARCHAR(255)
        )
        '''
    )

    for r in restaurants:
        cursor.execute(
            """INSERT INTO restaurants(name, link, phone_number, address, cuisine, cost, additional) 
            VALUES(%s, %s, %s, %s, %s, %s, %s)""",
            (r['Название'], r['Ссылка'], r['Номер телефона'], r['Адрес'], 
            r['Кухня'], r['Примерная цена'], r['Дополнительно'])
        )
    db.commit()

    cursor.execute(
        "SELECT * FROM restaurants"
    )
    restaurantsDb = cursor.fetchall()
    print(restaurantsDb)

except Exception as ex:
    print(ex)
finally:
    if (db.is_connected):
        cursor.close()
        db.close()
