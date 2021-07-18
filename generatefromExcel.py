import pandas as pd

class ExcelFile:

    def __init__(self, filename: str):
        self.file = pd.read_excel(filename)

