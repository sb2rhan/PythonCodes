import db_config
import mysql.connector


try:
    configs = db_config.config_db
    print(configs)
    db = mysql.connector.connect(**configs)

    mc = db.cursor()
    mc.execute('SELECT * FROM fibonacci')
    print(mc.fetchall())

except Exception as e:
    print(e)
finally:
    if db.is_connected():
        db.close()
