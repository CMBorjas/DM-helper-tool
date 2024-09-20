import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="dungeon_master"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE players (
        player_id INT AUTO_INCREMENT PRIMARY KEY,
        player_name VARCHAR(100),
        health INT,
        strength INT,
        dexterity INT,
        intelligence INT
    )
""")
# Create more tables for encounters, maps, etc.
db.commit()
