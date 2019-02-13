import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from graphs import score_by_game_dur, win_by_behind_ball_diff, \
    win_by_defensive_half, score_by_on_ground, score_by_slow_speed

external_stylesheets = ['https://unpkg.com/material-components-web@latest/dist/material-components-web.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Rocket League Analysis'),

    # html.Div(children='''
    #     Dash: A web application framework for Python.
    # '''),

    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Score by Game Duration', children=[
            score_by_game_dur
        ]),
        dcc.Tab(label='Outcome by Difference of Time Spent Behind Ball', children=[
            win_by_behind_ball_diff
        ]),
        dcc.Tab(label='Score by Time Spent in Own Defensive Half', children=[
            win_by_defensive_half
        ]),
        dcc.Tab(label='Score by Time Spent on The Ground', children=[
            score_by_on_ground
        ]),
        dcc.Tab(label='Score by Time Spent Travelling at a Slow Speed', children=[
            score_by_slow_speed
        ])
    ])
])



if __name__ == '__main__':
    app.run_server(debug=True)