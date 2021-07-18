import pandas as pd
import qrcode

import os


class ExcelQrCodeGenerator:

    def __init__(self, filename=None):
        self.directory_name_reference = None 
        
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
        self.directory_name_reference = name_column
        if not self.file_ready():
            raise TypeError("you have not loaded an Excel File yet")
        
        basePath = os.getcwd()
        self.outputs_directory = os.path.join(basePath, output_directory)
        if not os.path.exists(self.outputs_directory):
            os.mkdir(self.outputs_directory)

        names_column = self.file[name_column]
        for name in names_column:
            name_directory = os.path.join(self.outputs_directory, name)
            if not os.path.exists(name_directory):
                os.mkdir(name_directory)

    def generate(self, data_column_name, name_column_name=None):
        if self.directory_name_reference is None:
            raise TypeError('the directory Name Reference Column has not been set')

        data_column = self.file[data_column_name]
        directory_name_column = self.file[self.directory_name_reference]

        if name_column_name is None:
            name_column = [range(1, len(data_column))]
        else:
            name_column = self.file[name_column_name] 
        
        for i in range(len(data_column)):
           code = qrcode.make(data_column[i])
           path = os.path.join(self.outputs_directory, directory_name_column[i], f'{name_column[i]}.png') 
           code.save(path)






        
