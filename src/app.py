from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "root123"),
        database=os.environ.get("DB_NAME", "hola_db")
    )
    return connection

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 'Conexion exitosa a MySQL desde Flask con Docker Compose' AS mensaje;")
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        return f"""
        <h1>Hola Mundo</h1>
        <p>{result[0]}</p>
        """
    except Exception as e:
        return f"""
        <h1>Hola Mundo</h1>
        <p>Error conectando a MySQL: {str(e)}</p>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)