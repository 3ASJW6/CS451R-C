# Import <
import pyodbc
from dash import html, dcc, callback_context
from backEnd.API.Utility import parentQuery, childQuery, application
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# >

# note: we get a user's data in here
# and not in Login.py. in Login.py we
# set the data for a user.

# Declaration <
connection_string = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=451project.database.windows.net;"
    "Database=451_DB;"
    "UID=_db_;"
    "PWD=451Project;"
)
n_buttons = 5
cursor = connection_string.cursor()
info = parentQuery(cursor, "Event_Info", "*", ("",))
strInfo = str(info[0])

def generate_event_button(event):
    return dbc.Button(children=str(event["Title"]),
                      color="primary",
                      className="mr-1",
                      id=str(event["Title"]))

dashboardLayout = html.Div(id = 'dashboardLayoutId', children = [generate_event_button(i) for i in info] + [html.Div(id="log")])


@application.callback(Output("log", "children"), [Input(str(i["Title"]), "n_clicks") for i in info])
def func(*args):
    trigger = callback_context.triggered[0]
    return "You clicked button {}".format(trigger["prop_id"].split(".")[0])

# reference: https://dash.plotly.com/advanced-callbacks
# reference: https://stackoverflow.com/questions/62119605/dash-how-to-callback-depending-on-which-button-is-being-clicked





# >
