from django.shortcuts import render

import pandas as pd
import sqlite3

from plotly.offline import plot
from plotly.subplots import make_subplots

import plotly.graph_objects as go

DATABASE_FILE = "db.sqlite3"
HEIGHT_VIZ = 630


def index(request):
    """ Landing Page"""
    return render(request, 'velib/index.html')


def get_data(query):
    """ connect to database and execute query"""

    # connect to database
    con = sqlite3.connect(DATABASE_FILE)

    # store response in pandas DataFrame
    df = pd.read_sql_query(query, con)

    # close connection because we have the data we need
    con.close()
    return df


def viz1(request):
    """ first visualization"""
    
    query = """SELECT commune, count(commune) total
               FROM velib_station
               GROUP BY commune
               ORDER BY total desc"""
    df1 = get_data(query)

    # take 20 countries with most stations that are not Paris 
    # the data is already sorted using the sql query
    df2 = df1[df1["commune"] != "Paris"]
    df2 = df2.head(20)
    
    # any other commune is renamed "other communes"
    df1.loc[df1['commune'] != "Paris", 'commune'] = 'Other communes'
    
    
    
    # Plotting
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])
    fig.add_trace(go.Pie(values=df1['total'],labels=df1['commune'],title="Number of stations in Paris compared to other communes"),row=1, col=1)
    fig.add_trace(go.Pie(values=df2['total'],labels=df2['commune'],title="20 communes with most stations (besides Paris)"),row=1, col=2)

    fig.update_traces(textfont_size=20, marker={'line':
                                                {'color': '#000000', 'width': 2}})

    fig.update_layout({
        'title': 'Distribution of stations',
        'height': HEIGHT_VIZ,
    })

    plot_div = plot({'data': fig},
                    output_type='div')

    return render(request, 'velib/viz1.html', context={'plot_div': plot_div})


def viz2(request):
    """ second visualization"""
    query = """SELECT commune, is_installed
               FROM velib_station
               WHERE commune != 'Paris'"""
    df = get_data(query)

    # Plotting
    fig = go.Figure(data=go.Histogram(histfunc="sum",
                                      x=df["commune"],
                                      y=df["is_installed"],
                                      marker_color='#EB89B5'
                                      )).update_xaxes(categoryorder='total descending')

    fig.update_layout({
        'title': 'Active stations in different communes (besides Paris)',
        'height': HEIGHT_VIZ,
    })

    plot_div = plot({'data': fig},
                    output_type='div')

    return render(request, 'velib/viz2.html', context={'plot_div': plot_div})