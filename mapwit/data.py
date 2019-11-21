from flask import current_app as app
import pandas as pd
import jsonschema
import json
import os
import collections

DEMO_DATA = "data/demo_dataset.csv"
DATAFILES_PATH = "data/datapoints"
JSONSCHEMA_PATH = os.path.join("data", "mapwit_schema.json")
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def read_demo_data():
    df = pd.read_csv(app.open_resource(DEMO_DATA))
    df.head()
    return df


def read_datapoints_data():
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
    filepath = os.path.join(DATAFILES_PATH, filename)

    f = app.open_resource(JSONSCHEMA_PATH)
    schema = json.load(f)

    g = app.open_resource(filepath)
    json_data = json.load(g)

    jsonschema.validate(json_data, schema)

    return json_data
