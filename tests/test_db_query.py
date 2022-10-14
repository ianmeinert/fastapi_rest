import pyodbc
from core.config import Settings

server: str = ""
database: str = ""

conn = pyodbc.connect(Settings.DATABASE_URI)
cursor = conn.cursor()
cursor.execute("SELECT HOST_NAME() AS HostName, SUSER_NAME() LoggedInUser")

print(cursor.fetchone())
