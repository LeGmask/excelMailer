import pandas as pd
from pandas import DataFrame

pd.set_option('display.max_colwidth', 255)

class ExcelManager:
    def __init__(self, config):
        self.data: DataFrame | None = None
        self.config = config

        self.load_data()
        self.apply_filters()

    def load_data(self):
        self.data = pd.read_excel(self.config.get(['EXCEL', 'filepath']),
                                  sheet_name=self.config.get(['EXCEL', 'sheet_name']),
                                  header=self.config.get(['EXCEL', 'header']))
    def apply_filters(self):
        filters = self.config.get(['EXCEL', 'filters'])
        for excel_filter in filters:
            self.data = self.data[self.data[excel_filter['column']].isin(excel_filter['value'])]

    def __repr__(self):
        return self.data.__repr__()

