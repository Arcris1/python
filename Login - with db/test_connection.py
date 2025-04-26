import mysql.connector

print("Trying DB connect...")

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='login_system'
    )
    if conn.is_connected():
        print("✅ Connected to MySQL")
    else:
        print("❌ Failed to connect to MySQL")
except mysql.connector.Error as err:
    print(f"❌ MySQL Error: {err}")
except Exception as e:
    print(f"❌ General Exception: {e}")
