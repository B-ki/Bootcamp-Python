import pandas as pd


class FileLoader:
    def load(self, path: str):
        ret = pd.read_csv(path)
        print(ret.shape)
        return ret

    def display(self, df, n):
        if not isinstance(n, int):
            return
        print(df.head(n))
