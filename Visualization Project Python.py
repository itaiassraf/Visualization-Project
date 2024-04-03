# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:03:46 2022

@author: itaia
"""
import plotly.express as px
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd 
import plotly
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)
from PIL import Image
import dash_bootstrap_components as dbc

outlines_bounds = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-250',
    y0='-47.5',
    x1='250',
    y1='422.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
thebasket = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='7.5',
    y0='7.5',
    x1='-7.5',
    y1='-7.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
backboard = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-30',
    y0='-7.5',
    x1='30',
    y1='-6.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    ),
    fillcolor='rgba(10, 10, 10, 1)'
)
In_The_Paint = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-80',
    y0='-47.5',
    x1='80',
    y1='143.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
RA_the_small_circle = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-60',
    y0='-47.5',
    x1='60',
    y1='143.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
line_left_of_3_points = dict(
    type='line',
    xref='x',
    yref='y',
    x0='-220',
    y0='-47.5',
    x1='-220',
    y1='92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
line_right_of_3_points = dict(
    type='line',
    xref='x',
    yref='y',
    x0='220',
    y0='-47.5',
    x1='220',
    y1='92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
middle_3_points_line = dict(
    type='path',
    xref='x',
    yref='y',
    path='M -220 92.5 C -70 300, 70 300, 220 92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
center_line = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='60',
    y0='482.5',
    x1='-60',
    y1='362.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
small_circle_in_free_throw_line = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='20',
    y0='442.5',
    x1='-20',
    y1='402.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
FreeThrow = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='60',
    y0='200',
    x1='-60',
    y1='80',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
Restricted_Area_RA = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='40',
    y0='40',
    x1='-40',
    y1='-40',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1,
        dash='dot'
    )
)
basketball_court = [outlines_bounds,thebasket,backboard,In_The_Paint,RA_the_small_circle,line_left_of_3_points,line_right_of_3_points,middle_3_points_line,center_line,small_circle_in_free_throw_line,FreeThrow,Restricted_Area_RA]
df = pd.read_csv('21Seasons_Locations_top100_new (4).csv')
data=[]  

data1=go.Scattergl(
    x = df[(df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['ON_COURT_LOC_X'],
    y = df[(df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['ON_COURT_LOC_Y'],
    mode = 'markers',
    marker= dict(color='#f87c24', symbol='0', size=10, line={'width':1}, opacity=0.7),
    name = 'Above The break 3',
    text = "Total Shots: " + df[(df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['COUNT_THROWS_LOC'].astype(str)
      + "<br>Player's Name who threw the most : " + df[(df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['PLAYER_MOST_FREQUENCY_LOC'].astype(str) 
      + "<br>Biggest Amount Of Shots By a Player: " + round(df[(df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['AMOUNT_THROWS_OF_PLAYER_MOST_FREQUENCY_LOC'],3).astype(str)
      + "<br>field Goals%: " + round(df[(df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['FG_LOCATION'],3).astype(str),
      hoverinfo='text', 
      textfont = dict(
        color = 'rgba(75, 85, 102,0.7)')
    )
data2=go.Scattergl(
    x = df[(df['SHOT_ZONE_BASIC'] =='Mid-Range')]['ON_COURT_LOC_X'],
    y = df[(df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['ON_COURT_LOC_Y'],
    mode = 'markers',
    marker= dict(color='#bcbd22', symbol='0', size=10, line={'width':1}, opacity=0.7),
    name = 'Mid-Range',
    text = "Total Shots: " + df[(df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['COUNT_THROWS_LOC'].astype(str)
      + "<br>Player's Name who threw the most : " + df[(df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['PLAYER_MOST_FREQUENCY_LOC'].astype(str) 
      + "<br>Biggest Amount Of Shots By a Player: " + round(df[(df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['AMOUNT_THROWS_OF_PLAYER_MOST_FREQUENCY_LOC'],3).astype(str)
      + "<br>Field Goals%: " + round(df[(df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['FG_LOCATION'],3).astype(str),
      hoverinfo='text',
      textfont = dict(
        color = 'rgba(75, 85, 102,0.7)')
)

data3=go.Scattergl(
    x = df[(df['SHOT_ZONE_BASIC'] =='Restricted Area')]['ON_COURT_LOC_X'],
    y = df[(df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['ON_COURT_LOC_Y'],
    mode = 'markers',
    marker= dict(color='#17becf', symbol='0', size=10, line={'width':1}, opacity=0.7),
    name = 'Restricted Area',
    text = "Total Shots: " + df[(df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['COUNT_THROWS_LOC'].astype(str)
      + "<br>Player's Name who threw the most : " + df[(df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['PLAYER_MOST_FREQUENCY_LOC'].astype(str) 
      + "<br>Biggest Amount Of Shots By a Player: " + round(df[(df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['AMOUNT_THROWS_OF_PLAYER_MOST_FREQUENCY_LOC'],3).astype(str)
      + "<br>Field Goals%: " + round(df[(df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['FG_LOCATION'],3).astype(str),
      hoverinfo='text',
      textfont = dict(
        color = 'rgba(75, 85, 102,0.7)')
)
data4=go.Scattergl(
    x = df[(df['SHOT_ZONE_BASIC'] =='In The Paint (Non-RA)')]['ON_COURT_LOC_X'],
    y = df[(df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['ON_COURT_LOC_Y'],
    mode = 'markers',
    marker= dict(color='#e377c2', symbol='0', size=10, line={'width':1}, opacity=0.7),
    name = 'In The Paint',
    text = "Total Shots: " + df[(df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['COUNT_THROWS_LOC'].astype(str)
      + "<br>Player's Name who threw the most : " + df[(df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['PLAYER_MOST_FREQUENCY_LOC'].astype(str) 
      + "<br>Biggest Amount Of Shots By a Player: " + round(df[(df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['AMOUNT_THROWS_OF_PLAYER_MOST_FREQUENCY_LOC'],3).astype(str)
      + "<br>Field Goals%: " + round(df[(df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['FG_LOCATION'],3).astype(str),
      hoverinfo="text",
      textfont = dict(
        color = 'rgba(75, 85, 102,0.7)')
)

data.append(data1)
data.append(data2)
data.append(data3)
data.append(data4)

layout = go.Layout(
title='Shot Chart',
titlefont=dict(
    size=14
),
hovermode = 'closest',
showlegend = True,
height = 600,
width = 600, 
shapes = basketball_court,
xaxis = dict(
    showticklabels = False,
    range = [-250, 250]
),
yaxis = dict(
    showticklabels = False,
    range = [-47.5, 452.5]
)
)

fig1=go.Figure(data=data,layout=layout)
fig1.update_layout(transition_duration=500)

data2=[]
df2=pd.read_csv('each_area_relation (1).csv')

data5=go.Scattergl(
    x = df2['year'],
    y = df2['3Points_Shots_To_All_Shots'],
    mode = 'lines',
    marker= dict(color='#f87c24', symbol='0', size=10, line={'width':1}, opacity=0.7),
    name = 'Above The break 3',
    text = "Above The break 3: " + round(df2['3Points_Shots_To_All_Shots'],3).astype(str),
      hoverinfo='text', 
      textfont = dict(
        color = 'rgba(75, 85, 102,0.7)')
    )
data6=go.Scattergl(
    x = df2['year'],
    y = df2['MID_Points_Shots_To_All_Shots'],
    mode = 'lines',
    marker= dict(color='#bcbd22',line={'width':1}, opacity=0.7),
    name = 'Mid-Range',
    text = "Mid-Range: " + round(df2['MID_Points_Shots_To_All_Shots'],3).astype(str),
      hoverinfo='text', 
      textfont = dict(
        color = 'rgba(75, 85, 102,0.7)')
    )

data7=go.Scattergl(
    x = df2['year'],
    y = df2['RESTRICT_Points_Shots_To_All_Shots'],
    mode = 'lines',
    marker= dict(color='#17becf', line={'width':1}, opacity=0.7),
    name = 'Restricted Area',
    text = "Restricted Area: " + round(df2['RESTRICT_Points_Shots_To_All_Shots'],3).astype(str),
      hoverinfo='text', 
      textfont = dict(
        color = 'rgba(75, 85, 102,0.7)')
    )
data8=go.Scattergl(
    x = df2['year'],
    y = df2['PAINT_Points_Shots_To_All_Shots'],
    mode = 'lines',
    marker= dict(color='#e377c2',line={'width':1}, opacity=0.7),
    name = 'In The Paint',
    text = "In The Paint: " + round(df2['PAINT_Points_Shots_To_All_Shots'],3).astype(str),
      hoverinfo='text', 
      textfont = dict(
        color = 'rgba(75, 85, 102,0.7)')
    )

data2=[data5,data6,data7,data8]

layout2 = go.Layout(
title='Shot Chart',
titlefont=dict(
    size=14
),
hovermode = 'x', 
showlegend = True
)

fig2=go.Figure(data=data2,layout=layout2)
fig2.update_layout(transition_duration=500)
fig2=go.Figure(data=data2,layout=layout2)
fig2.update_layout(transition_duration=500)
app = dash.Dash()
app.layout = html.Div(
        children=[html.Div(
            children=[
                html.P(children="Somewhere Over the Rainbow 🌈🏀", style={'fontSize': "40px",'textAlign': 'center'}, className="header-emoji"), #emoji
                html.H1(
                    children="The NBA Revolution ",style={'textAlign': 'center'}, className="header-title" 
                ), #Header title
                html.H2(
                    children="Analysis of the 100 Locations"
                    " where the most shots were thrown"
                    " between the years 2000 and 2020",
                    className="header-description", style={'textAlign': 'center'},
                ),
            ],
            className="header",style={'backgroundColor':'#F5F5F5'},
        ),
                   
            html.Div(
                children = dcc.Graph(
                    id = 'Shot_Chart_basketball',
                    figure = fig1,
                ),
                style={'width': '50%', 'display': 'inline-block'},
            ),
                html.Div(
                children = dcc.Graph(
                    id = 'Line',
                    figure = fig2,
                ),
                style={'width': '50%', 'display': 'inline-block'},
            ),
          
            html.Div([
            html.Label(['Choose a Year:'],
            style={'font-weight': 'bold'}),
            html.P(),
            dcc.Slider(
                df['season'].min(),
                df['season'].max(),
                step=None,
                value=df['season'].min(),
                marks={str(year): str(year) for year in df['season'].unique()},
                id='year-slider'
            ),
        ],
        className = 'double-graph',
        ),
    ])


@app.callback(
    Output('Shot_Chart_basketball', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    data=[]
    filtered_df = df[df.season == selected_year]

    data1=go.Scattergl(
        x = filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['ON_COURT_LOC_X'],
        y = filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['ON_COURT_LOC_Y'],
        mode = 'markers',
        marker= dict(color='#f87c24', symbol='0', size=10, line={'width':1}, opacity=0.7),
        name = 'Above The break 3',
        text = "<b>Player's Name who threw the most : " + filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['PLAYER_MOST_FREQUENCY_LOC'].astype(str)+"      </b>" 
         +"<br><b>Total Shots: " + filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['COUNT_THROWS_LOC'].astype(str)
         + "<br><b>Biggest Amount Of Shots By a Player: " + round(filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['AMOUNT_THROWS_OF_PLAYER_MOST_FREQUENCY_LOC'],3).astype(str)
         + "<br><b>Location's Field Goals%: " + round(filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Above The break 3')]['FG_LOCATION'],3).astype(str),
         hoverinfo='text', 
         textfont = dict(
            color = 'rgba(75, 85, 102,0.7)')
        )
    data2=go.Scattergl(
        x = filtered_df[(filtered_df['SHOT_ZONE_BASIC'] =='Mid-Range')]['ON_COURT_LOC_X'],
        y = filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['ON_COURT_LOC_Y'],
        mode = 'markers',
        marker= dict(color='#bcbd22', symbol='0', size=10, line={'width':1}, opacity=0.7),
        name = 'Mid-Range',
        text = "<b>Player's Name who threw the most : " + filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['PLAYER_MOST_FREQUENCY_LOC'].astype(str)+"      </b>"  
         + "<br><b>Total Shots: " + filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['COUNT_THROWS_LOC'].astype(str)
         + "<br><b>Biggest Amount Of Shots By a Player: " + round(filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['AMOUNT_THROWS_OF_PLAYER_MOST_FREQUENCY_LOC'],3).astype(str)
         + "<br><b>Location's Field Goals%: " + round(filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Mid-Range')]['FG_LOCATION'],3).astype(str),
         hoverinfo='text',
         textfont = dict(
            color = 'rgba(75, 85, 102,0.7)')
    )

    data3=go.Scattergl(
        x = filtered_df[(filtered_df['SHOT_ZONE_BASIC'] =='Restricted Area')]['ON_COURT_LOC_X'],
        y = filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['ON_COURT_LOC_Y'],
        mode = 'markers',
        marker= dict(color='#17becf', symbol='0', size=10, line={'width':1}, opacity=0.7),
        name = 'Restricted Area',
        text = "<b>Player's Name who threw the most : " + filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['PLAYER_MOST_FREQUENCY_LOC'].astype(str)+"      </b>"  
         + "<br><b>Total Shots: " + filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['COUNT_THROWS_LOC'].astype(str)
         + "<br><b>Biggest Amount Of Shots By a Player: " + round(filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['AMOUNT_THROWS_OF_PLAYER_MOST_FREQUENCY_LOC'],3).astype(str)
         + "<br><b>Location Field Goals%: " + round(filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'Restricted Area')]['FG_LOCATION'],3).astype(str),
         hoverinfo='text',
         textfont = dict(
            color = 'rgba(75, 85, 102,0.7)')
    )
    data4=go.Scattergl(
        x = filtered_df[(filtered_df['SHOT_ZONE_BASIC'] =='In The Paint (Non-RA)')]['ON_COURT_LOC_X'],
        y = filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['ON_COURT_LOC_Y'],
        mode = 'markers',
        marker= dict(color='#e377c2', symbol='0', size=10, line={'width':1}, opacity=0.7),
        name = 'In The Paint',
        text ="<b>Player's Name who threw the most : " + filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['PLAYER_MOST_FREQUENCY_LOC'].astype(str)+"      </b>"   
         + "<br><b>Total Shots: " + filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['COUNT_THROWS_LOC'].astype(str)
         + "<br><b>Biggest Amount Of Shots By a Player: " + round(filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['AMOUNT_THROWS_OF_PLAYER_MOST_FREQUENCY_LOC'],3).astype(str)
         + "<br><b>Location Field Goals%: " + round(filtered_df[(filtered_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)')]['FG_LOCATION'],3).astype(str),
         hoverinfo="text",
         textfont = dict(
            size=8,
            color = 'rgba(75, 85, 102,0.7)')
    )
    
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)
    
    full_season=str(selected_year-1) + '-' + str(selected_year)

    layout = go.Layout(
    title=go.layout.Title(
        text=f'100 Locations Where The Most Shots Were Thrown <br><sup>On {full_season} Season</sup>',
        xref="paper",
        x=0,  
        font=dict(
        size=18
    )
    ),
    hovermode = 'closest',
    showlegend = True,
    height = 650,
    width = 685, 
    shapes = basketball_court,
    
    xaxis = dict(
        showticklabels = False,
        range = [-250, 250],
        # title=go.layout.xaxis.Title(
        #     text="Horizontal location",
        #     font=dict(
        #         size=18
        #     )
    ),
    yaxis = dict(
        showticklabels = False,
        range = [-47.5, 452.5]
        # title=go.layout.yaxis.Title(
        #   text="Vertical Location",
        #   font=dict(
        #       size=18
        #     )
        # )
    )
    )
    

    fig=go.Figure(data=data,layout=layout)
    fig.update_layout(transition_duration=500,legend_title_text = 'Areas') 
    pyLogo = Image.open("half.jpg")
    fig.add_layout_image(
        dict(
            source=pyLogo,
            xref="x",
            yref="y",
            x=-500,
            y=1000,
            sizex=5000,
            sizey=2000,
            sizing="stretch",
            opacity=0.5,
            layer="below"))  
         
    return fig

@app.callback(
    Output('Line', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    data2=[]
    filtered_df2 = df2[df2.season == selected_year]
    data5=go.Scattergl(
        x = filtered_df2['year'],
        y = filtered_df2['3Points_Shots_To_All_Shots'],
        mode = 'lines+markers',
        marker= dict(color='#f87c24', symbol='0', size=10, line={'width':1}, opacity=0.7),
        name = 'Above The Break 3',
        text = "Above The Break 3: " + round(filtered_df2['3Points_Shots_To_All_Shots'],3).astype(str),
          hoverinfo='text', 
          textfont = dict(
            color = 'rgba(75, 85, 102,0.7)')
        )
    data6=go.Scattergl(
        x = filtered_df2['year'],
        y = filtered_df2['MID_Points_Shots_To_All_Shots'],
        mode = 'lines+markers',
        marker= dict(color='#bcbd22',line={'width':1},size=10, opacity=0.7),
        name = 'Mid-Range',
        text = "Mid-Range: " + round(filtered_df2['MID_Points_Shots_To_All_Shots'],3).astype(str),
          hoverinfo='text', 
          textfont = dict(
            color = 'rgba(75, 85, 102,0.7)')
        )

    data7=go.Scattergl(
        x = filtered_df2['year'],
        y = filtered_df2['RESTRICT_Points_Shots_To_All_Shots'],
        mode = 'lines+markers',
        marker= dict(color='#17becf',size=10, line={'width':1}, opacity=0.7),
        name = 'Restricted Area',
        text = "Restricted Area: " + round(filtered_df2['RESTRICT_Points_Shots_To_All_Shots'],3).astype(str),
          hoverinfo='text', 
          textfont = dict(
            color = 'rgba(75, 85, 102,0.7)')
        )
    data8=go.Scattergl(
        x = filtered_df2['year'],
        y = filtered_df2['PAINT_Points_Shots_To_All_Shots'],
        mode = 'lines+markers',
        marker= dict(color='#e377c2',size=10,line={'width':1}, opacity=0.7),
        name = 'In The Paint',
        text = "In The Paint: " + round(filtered_df2['PAINT_Points_Shots_To_All_Shots'],3).astype(str),
          hoverinfo='text', 
          textfont = dict(
            color = 'rgba(75, 85, 102,0.7)')
        )

    data2=[data5,data6,data7,data8]

    layout2 = go.Layout(
    title=go.layout.Title(
        text='The Change In The Ratio Of Shots From Each Area <br><sup> Ratio Of Shots Thrown From Area To The Total Amount Of Shots</sup>',
        xref="paper",
        x=0,  
        font=dict(
        size=18
    )
    ),
    hovermode = "x", 
    showlegend = True,
    height = 650,
    width = 650, 
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Year",
            font=dict(
                size=18
            )
        ),
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Ratio Of The Amount Of Shots",
            font=dict(
                size=18
            )
        )
    )
    )
    

    fig2=go.Figure(data=data2,layout=layout2,layout_xaxis_range=[1999,2021])
    fig2.update_layout(transition_duration=500,legend_title_text = 'Areas',legend_tracegroupgap= 60)
    pyLogo = Image.open("half.jpg")
    fig2.add_layout_image(
        dict(
            source=pyLogo,
            xref="x",
            yref="y",
            x=0,
            y=1000,
            sizex=2500,
            sizey=2000,
            sizing="stretch",
            opacity=0.5,
            layer="below")
      )
    
    fig2.update_layout(hovermode="x")
   

    return fig2



if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=False)