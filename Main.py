# Import <
import pyodbc
from backEnd.API.User import User
from backEnd.API.Event import Event
from backEnd.API.Course import Course
from backEnd.API.Member import Member
from backEnd.API.Location import Location
from backEnd.API.Utility import application, parentQuery, childQuery, joinQuery
from frontEnd.Layout.Login import loginLayout
from frontEnd.Layout.Event import eventLayout
# >

connection_string = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=451project.database.windows.net;"
            "Database=451_DB;"
            "UID=_db_;"
            "PWD=451Project;"
)
cursor = connection_string.cursor()

if __name__ == '__main__':
    application.layout = eventLayout
    application.run_server(debug = True)



