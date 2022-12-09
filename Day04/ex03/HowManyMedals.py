import pandas as pd
import numpy as np


def how_many_medals(df, name):
    d1 = df[df.Name == name]
    dict = {}
    for y in d1.Year.drop_duplicates():
        new_dict = {y: {
            'G': d1[(d1.Year == y) & (d1.Medal == 'Gold')].count()[0],
            'S': d1[(d1.Year == y) & (d1.Medal == 'Silver')].count()[0],
            'B': d1[(d1.Year == y) & (d1.Medal == 'Bronze')].count()[0]}}
        dict.update(new_dict)
    return dict
