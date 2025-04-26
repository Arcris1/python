import MySQLdb

class Connection:
    
    def __init__(self):
        self.connection = None
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'passwd': '',  # Note: mysqlclient uses 'passwd' instead of 'password'
            'db': 'login_system',  # Note: mysqlclient uses 'db' instead of 'database'
        }

    def connect(self):
        print("🔌 connect() called...")
        print(f"🛠️ Using config: {self.config}")
        try:
            if self.connection:
                print("🔁 Closing previous connection...")
                self.close()

            print("🔄 Attempting new connection...")
            self.connection = MySQLdb.connect(**self.config)
            
            if self.connection.open:  # mysqlclient uses .open instead of .is_connected()
                print("✅ Successfully connected to MySQL!")
                self.connection.autocommit(True)  # Note: method call instead of property
                return self.connection
            else:
                print("❌ Connection object created but not connected!")
                return None

        except MySQLdb.Error as err:  # Changed exception type
            print(f"❌ MySQL Error: {err}")
            print(f"🔧 Error Code: {err.args[0]}")  # Error code is in args[0]
            return None
        except Exception as e:
            print(f"❌ Unexpected Error: {repr(e)}")
            import traceback
            traceback.print_exc()
            return None

    def close(self):
        if self.connection and self.connection.open:  # Changed to .open
            self.connection.close()
            print("✅ Database connection closed.")
        else:
            print("⚠️ No active connection to close.")