import time
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)
CORS(app)

def create_connection():
    while True:
        try:
            conn = psycopg2.connect(
                dbname="newsDB",
                user="postgres",
                password="1234",
                host="postgres-container",
                port="5432"
            )
            print("Connected to PostgreSQL")
            return conn
        except OperationalError:
            print("Waiting for PostgreSQL to be ready...")
            time.sleep(5)


conn = create_connection()
cursor = conn.cursor()


@app.route('/getUrgentNews', methods=['GET'])
def get_urgent_news():
    cursor.execute("SELECT * FROM news ORDER BY id ASC LIMIT 10;")
    news = cursor.fetchall()
    cursor.execute("SELECT current_database();")
    db_name = cursor.fetchone()
    print("Connected to Database:", db_name)

    if not news:
        return jsonify({"message": "No news available"}), 404

    return jsonify([{"id": row[0], "title": row[1], "content": row[2]} for row in news])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
