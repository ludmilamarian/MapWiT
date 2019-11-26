# -*- coding: utf-8 -*-
#
# This file is part of MapWiT.
# Copyright (c) 2019 The MapWiT Authors
#
# MapWiT is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import collections
import json
import os

import jsonschema
import pandas as pd
from flask import current_app as app

# path to the demp data file
DEMO_DATA = "data/demo_dataset.csv"

# path to the folder containing the data points
DATAFILES_PATH = "data/datapoints"

# path to the JSON schema
JSONSCHEMA_PATH = os.path.join("data", "mapwit_schema.json")

# path to the root of the application
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def read_demo_data():
    """
    Reads the demo data file into a Panda DataFrame
    :return: The demo dataframe
    """
    df = pd.read_csv(app.open_resource(DEMO_DATA))
    df.head()
    return df


def read_datapoints_data():
    """
    Reads the data points files found in the `/data/datapoints` folder and
    converts them to a Panda DataFrame
    :return: The datapoints as a DataFrame
    """

    data_keys = {
        "CountryOfLiving": "Live",
        "CountryOfBirth": "Born",
        "index": "Country",
    }

    data_intermediate = collections.defaultdict(list)

    for filename in os.listdir(os.path.join(APP_ROOT, DATAFILES_PATH)):
        json_data = validate_datapoint(filename)
        for k, v in json_data.items():
            data_intermediate[k].append(v)

    counted_data = {}
    for k, v in data_intermediate.items():
        counted_data[k] = collections.Counter(v)

    df = pd.DataFrame(counted_data)  # currently the index is the Country
    df.reset_index(level=0, inplace=True)  # add another index, 0..n
    df.rename(columns=data_keys, inplace=True)  # rename the lables of the columns
    df.fillna(0, inplace=True)  # fill NaN with 0

    return df


def validate_datapoint(filename):
    """
    Validates all the datapoint files agains the JSON schema;
    The function will raise an error if one of the datafiles is not valid.
    :return: a json object with the data from `filename`

    """
    filepath = os.path.join(DATAFILES_PATH, filename)

    f = app.open_resource(JSONSCHEMA_PATH)
    schema = json.load(f)

    g = app.open_resource(filepath)
    json_data = json.load(g)

    jsonschema.validate(json_data, schema)

    return json_data
