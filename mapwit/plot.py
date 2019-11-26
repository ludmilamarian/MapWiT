# -*- coding: utf-8 -*-
#
# This file is part of MapWiT.
# Copyright (c) 2019 The MapWiT Authors
#
# MapWiT is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import plotly.graph_objects as go
from plotly.offline import plot

from . import data


def create_map(df):
    """
    Creates the world map and adds traces for total, born and live.
    `df`: panda dataframe for the available data
    """

    colors = ["#8860D0", "#3AAFA9"]

    fig = go.Figure()

    fig.add_trace(
        go.Choropleth(
            locationmode="country names",
            locations=df["Country"],
            z=df["Born"] + df["Live"],
            text="",
            colorscale="Reds",
            autocolorscale=False,
            marker_line_color="white",  # line markers between states
            colorbar_title="Total participation",
            name="Total",
        )
    )

    for i, type in enumerate(["Born", "Live"]):
        fig.add_trace(
            go.Scattergeo(
                locationmode="country names",
                locations=df["Country"],
                text=df[type],
                marker=dict(
                    size=df[type] * 10, color=colors[i], sizemode="area", line_width=0
                ),
                name=type,
            )
        )

    fig.update_layout(
        title=go.layout.Title(
            text='Participation to the Workshop "Contributing to Open Source" - <a href="https://www.europeanwomenintech.com">EWiT</a>'
        ),
        geo=dict(
            landcolor="rgb(217, 217, 217)",
            showcoastlines=True,
            showcountries=True,
            coastlinecolor="white",
            countrycolor="white",
            projection_type="equirectangular",
            showframe=False,
            showlakes=True,
            lakecolor="rgb(255, 255, 255)",
        ),
        width=1400,
        height=800,
    )
    fig.update_layout(legend_orientation="h", legend=go.layout.Legend(x=0, y=1))

    plot_div = plot(fig, output_type="div")
    return plot_div


def create_demo_map():
    """
    Loads the demo dataset and creates the map
    :returns: The map, in html, with the traces
    """
    df = data.read_demo_data()
    return create_map(df)


def create_datapoints_map():
    """
    Load the data provided via the contributions,
    and create the map
    :returns: The map, in html, with the traces
    """
    df = data.read_datapoints_data()
    return create_map(df)
