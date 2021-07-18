from generatefromExcel import ExcelFile 

import unittest

class ExcelFileTestCase(unittest.TestCase):
    def setUp(self):
        self.file = ExcelFile()


if __name__ == "__main__":
    unittest.main()