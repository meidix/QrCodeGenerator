import pandas as pd

import os


class ExcelQrCodeGenerator:

    def __init__(self, filename=None):
        if filename is not None:
            try:
                self.file = pd.read_excel(filename)
            except TypeError:
                self.ready = False
                return Exception('the file does not exist')
            self.ready = True
        else:
            self.ready = False
        

    def file_ready(self):
        return self.ready

    def set_directory_name_reference(self, name_column: str, output_directory : str ='output'):
        if not self.file_ready():
            raise TypeError("you have not loaded an Excel File yet")
        
        basePath = os.getcwd()
        outputs_directory = os.path.join(basePath, output_directory)
        os.mkdir(outputs_directory)

        names_column = self.file[name_column]
        for name in names_column:
            name_directory = os.path.join(outputs_directory, name)
            if not os.path.exists(name_directory):
                os.mkdir(name_directory)





        
