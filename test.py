from qrCodeGenerator import ExcelQrCodeGenerator

import pandas as pd

import os
import unittest

class ExcelQrCodeGeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.generator = ExcelQrCodeGenerator(filename='test_file.xls')

    def test_TheExceFileLoads(self, *args, **kwargs):
        self.assertTrue(self.generator.file_ready())
    
    def test_directoriesAreCreatedAccordingToColumnName(self, *args, **kwargs):
        self.generator.set_directory_name_reference('Name')

        # checking the directory existance of results 
        working_directory = os.getcwd()
        outputs_directory = os.path.join(working_directory, 'output')
        self.assertTrue(os.path.exists(outputs_directory))

        excelFile = pd.read_excel('test_file.xls')
        names_column = excelFile['Name']

        # checking the if directories are created based on the Column 
        for name in names_column:
            directory = os.path.join(outputs_directory, name)
            self.assertTrue(os.path.exists(directory))






if __name__ == "__main__":
    unittest.main()