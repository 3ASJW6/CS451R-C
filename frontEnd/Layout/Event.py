# Import <
from dash import html, dcc
from dash.dependencies import Input, Output, State
from backEnd.API.Utility import getJSON, application, Login, Verify
import dash_bootstrap_components as dbc

# >


# Declaration <
style = getJSON(file = '/frontEnd/Resource/Event.json')
eventLayout = html.Div(
    [
        dbc.Button("Open modal", id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Alex Omorodion", style = style['headerStyle'])),
                dbc.ModalBody(
                    [
                        html.Div(id = 'eventLayout',
                                 children = [
                                     dcc.Tabs(id="event-tabs", value='tab-1-example-graph', children=[
                                         dcc.Tab(label='DETAILS', value='details-tab'),
                                         dcc.Tab(label='PERSON INFO', value='person-info-tab'),
                                     ]),
                                     html.Div(id='tabs-content-example-graph')
                                 ])
                    ]
                ),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)


@application.callback(
    Output("tabs-content-example-graph", "children"),
    Input('event-tabs', 'value'),
)
def render_content(tab):
    if tab == 'details-tab':
        return html.Div([
            html.Div("Yesterday at 4:00pm"),
            html.Div("Scheduled: on 11-29-2021 at 12:06am"),
            html.Div("Zoom link: Tutor will email"),
            html.Div("CompSci Assignments")
        ])
    elif tab == 'person-info-tab':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])

@application.callback(
    Output("modal", "is_open"),
    Input("open", "n_clicks"),
    Input("close", "n_clicks"),
    State("modal", "is_open")
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
