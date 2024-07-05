import glob
import os
import json
import re
import pandas as pd

def get_column_names(schemas, ds_name, sorting_key='column_position'):
    column_details = schemas[ds_name]
    columns = sorted(column_details, key=lambda col: col[sorting_key])
    return [col['column_name'] for col in columns]