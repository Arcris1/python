from config.Connection import Connection

class User:
    def register_user(self, username, password, gender):
        print("⏳ Creating DB connection...")
        db = Connection() 
        print("✅ Connection object created.")

        conn = db.connect()
        print("✅ connect() called.")

        cursor = None  
        print(f"🟢 Attempting to register user: {username}, {gender}")

        if not conn:
            print("❌ Database connection failed.")
            return False

        try:
            cursor = conn.cursor()
            sql = "INSERT INTO users (username, password, gender) VALUES (%s, %s, %s)"
            values = (username, password, gender)
            cursor.execute(sql, values)
            return True
        except Exception as e:
            print(f"❌ Failed to register user: {e}")
            return False
        finally:
            if cursor:
                try:
                    cursor.close()
                except Exception as e:
                    print(f"⚠️ Failed to close cursor: {e}")
            db.close()
            print("✅ Database connection closed.")
            
    def validate_user(self, username, password):
        db = Connection() 
        conn = db.connect()
        cursor = None  
        if not conn:
            return False

        try:
            cursor = conn.cursor()
            sql = "SELECT username, password FROM users WHERE username = %s AND password = %s"
            values = (username, password)
            cursor.execute(sql, values)
            
            result = cursor.fetchone()
            if not result:
                print("⚠️ User not found.")
                return False
            return True
        except Exception as e:
            print(f"❌ Failed to register user: {e}")
            return False
        finally:
            db.close()
            print("✅ Database connection closed.")
            
    def get_all_users(self):
        db = Connection() 
        conn = db.connect()
        cursor = None  
        if not conn:
            return False

        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            
            # Get users as a list of dictionaries
            columns = [column[0] for column in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            if not result:
                print("⚠️ No users found.")
                return False
            return result
        except Exception as e:
            print(f"❌ Failed to fetch users: {e}")
            return False
        finally:
            db.close()
            print("✅ Database connection closed.")
        
    def delete_user(self, user_id: int):
        db = Connection() 
        conn = db.connect()
        cursor = None  
        if not conn:
            return False

        try:
            cursor = conn.cursor()
            sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, (user_id))
            conn.commit()  # Commit the changes to the database
            
            if cursor.rowcount == 0:
                print("⚠️ No user found with the given ID.")
                return False
            print("✅ User deleted successfully.")
            return True

        except Exception as e:
            print(f"❌ Failed to fetch users: {e}")
            return False
        finally:
            db.close()
            print("✅ Database connection closed.")
        
