import mysql.connector

class DBConnect:
    def get_Connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Amrithasuku@123",
                database="companydb"
            )
            return self.connection
        except Exception as e:
            print(e)
connection_instance = DBConnect()
connection_instance.get_Connection()