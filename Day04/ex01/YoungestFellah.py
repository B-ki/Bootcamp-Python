import pandas as pd
import numpy as np


def youngest_fellah(df, year):
    women = df[(df['Year'] == year) & (df['Sex'] == 'F')]
    men = df[(df['Year'] == year) & (df['Sex'] == 'M')]
    return {'YoungestWomen': women['Age'].min(), 'YoungestMan':men['Age'].min()}
