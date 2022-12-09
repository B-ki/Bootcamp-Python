import pandas as pd
import numpy as np


def proportion_by_sport(df, year, sport, gender):
    df1 = df[(df['Year'] == year) & (df['Sex'] == gender)]
    df1 = df1.drop_duplicates(subset="ID")
    return df1[df1.Sport == sport].size / df1.size
