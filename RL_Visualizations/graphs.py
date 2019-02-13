import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import pandas as pd

df = pd.read_hdf('../champ_clean_not_scaled.h5')
df = df.drop(['team', 'game_id'], axis=1)
df = df[['score', 'game_duration', 'time_behind_ball_diff',
                        'saves', 'time_in_front_of_ball', 'time_defensive_half',
                        'time_on_ground', 'total_distance', 'time_low_in_air',
                        'time_neutral_third_diff', 'time_high_in_air_diff',
                        'time_defensive_third', 'avg_distance_to_ball_has_possession_diff',
                        'time_slow_speed', 'avg_distance_to_ball_no_possession',
                        'total_distance_diff', 'amount_collected_diff', 'time_behind_ball',
                        'win']]


lose = df[df['win'] == 0]
win = df[df['win'] == 1]


score_by_game_dur = dcc.Graph(
        id='score_by_game_duration',
        figure={
            'data':[
                go.Scatter(
                    x=win['game_duration'],
                    y=win['score'],
                    mode='markers',
                    name='Win',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(19, 81, 249)' #blue
                    },
                ),
                go.Scatter(
                    x=lose['game_duration'],
                    y=lose['score'],
                    mode='markers',
                    name='Loss',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(224, 18, 11)' #red
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear', 'title': 'Game Duration'},
                yaxis={'type': 'linear', 'title': 'Score'},
                legend={'x': 0, 'y': 1}
            )
        }
    )

win_by_behind_ball_diff = dcc.Graph(
        id='win_behind_ball_diff',
        figure={
            'data':[
                go.Scatter(
                    x=win.index,
                    y=win['time_behind_ball_diff'],
                    mode='markers',
                    name='Win',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(19, 81, 249)' #blue
                    },
                ),
                go.Scatter(
                    x=lose.index,
                    y=lose['time_behind_ball_diff'],
                    mode='markers',
                    name='Loss',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(224, 18, 11)' #red
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear', 'title': 'Difference of Time Spent Behind Ball'},
                yaxis={'type': 'linear', 'title': 'Game ID'},
                legend={'x': 0, 'y': 1}
            )
        }
    )

win_by_defensive_half = dcc.Graph(
        id='win_defensive_half',
        figure={
            'data':[
                go.Scatter(
                    x=win['score'],
                    y=win['time_defensive_half'],
                    mode='markers',
                    name='Win',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(19, 81, 249)' #blue
                    },
                ),
                go.Scatter(
                    x=lose['score'],
                    y=lose['time_defensive_half'],
                    mode='markers',
                    name='Loss',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(224, 18, 11)' #red
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear', 'title': 'Score'},
                yaxis={'type': 'linear', 'title': 'Time Spent in Defensive Half'},
                legend={'x': 0, 'y': 1}
            )
        }
    )

temp_win = win[win['time_on_ground'] != 0]
temp_lose = lose[lose['time_on_ground'] != 0]

score_by_on_ground = dcc.Graph(
        id='score_ground_time',
        figure={
            'data':[
                go.Scatter(
                    x=temp_win['score'],
                    y=temp_win['time_on_ground'],
                    mode='markers',
                    name='Win',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(19, 81, 249)' #blue
                    },
                ),
                go.Scatter(
                    x=temp_lose['score'],
                    y=temp_lose['time_on_ground'],
                    mode='markers',
                    name='Loss',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(224, 18, 11)' #red
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear', 'title': 'Score'},
                yaxis={'type': 'linear', 'title': 'Time Spent on the Ground'},
                legend={'x': 0, 'y': 1}
            )
        }
    )

score_by_slow_speed = dcc.Graph(
        id='score_slow_speed',
        figure={
            'data':[
                go.Scatter(
                    x=win['score'],
                    y=win['time_slow_speed'],
                    mode='markers',
                    name='Win',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(19, 81, 249)' #blue
                    },
                ),
                go.Scatter(
                    x=lose['score'],
                    y=lose['time_slow_speed'],
                    mode='markers',
                    name='Loss',
                    opacity=0.7,
                    marker={
                        'size':3,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(224, 18, 11)' #red
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear', 'title': 'Score'},
                yaxis={'type': 'linear', 'title': 'Time Spent Travelling at a Slow Speed'},
                legend={'x': 0, 'y': 1}
            )
        }
    )