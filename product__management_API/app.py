from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

db_config = {
    "host": "",
    "user": "",  
    "password": "", 
    "database": ""  
}


def fetch_products():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)  
        
        
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        
        return products

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route("/api/products", methods=["GET"])
def get_products():
    products = fetch_products()
    return jsonify({"products": products})

if __name__ == "__main__":
    app.run(debug=True)
