import psycopg2
import json
from psycopg2 import Error
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/enterText', methods=['GET'])
def getText1():
    try:
        connection = psycopg2.connect(user = "root2",
                                      password = "",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "postgres")

        cursor = connection.cursor()

        cursor.execute("INSERT INTO table_user (user_text,user_name) VALUES ('%s','%s')" % (request.args.get('mirrorText'),request.args.get('username')))
        cursor.execute("select user_text from table_user")
        records = cursor.fetchall()

        cursor.close()
        connection.commit()
        #print ("Successful")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print ("PostgreSQL connection is closed")
    return json.dumps(records)

@app.route('/frontend', methods=['GET'])
def getText():
    return render_template('WebForm.html')

if __name__ == "__main__":
    app.run()
