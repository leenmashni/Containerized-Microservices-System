import mysql.connector

# MySQL configuration
db_config = {
    'host': 'mysql-db',
    'user': 'leen',
    'password': 'Leen@2004',
    'database': 'video_db'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    path VARCHAR(255) NOT NULL
)
""")

conn.commit()
cursor.close()
conn.close()

