from flask import Flask, request, jsonify
import pandas as pd
import sqlalchemy as sa

app = Flask(__name__)

# Database setup
DATABASE_URI = 'sqlite:///zomato.db'  # Use SQLite for simplicity
engine = sa.create_engine(DATABASE_URI)
metadata = sa.MetaData()

# Define a function to create the table if it doesn't exist
def create_table():
    with engine.connect() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS restaurant (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            rating FLOAT
        )
        """)
    print("Table created or already exists.")

@app.route('/data', methods=['GET'])
def get_data():
    with engine.connect() as conn:
        query = "SELECT * FROM restaurant"
        df = pd.read_sql(query, conn)
    return jsonify(df.to_dict(orient='records'))

@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    df = pd.DataFrame(data)
    df.to_sql('restaurant', engine, if_exists='append', index=False)
    return jsonify({"message": "Data added successfully."}), 201

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
