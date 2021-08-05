import pandas as pd
import qrcode

import os

from imageGenerator import ImageGenerator


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

        data_column, directory_name_column, name_column = self.__prepare_columns_info(data_column_name, name_column_name)

        for i in range(len(data_column)):
            self._generate(data_column[i], directory_name_column[i], name_column[i], index=i)

    def __prepare_columns_info(self, data_column_name, name_column_name):
        data_column = self.file[data_column_name]
        directory_name_column = self.file[self.directory_name_reference]

        if name_column_name is None:
            name_column = [range(1, len(data_column))]
        else:
            name_column = self.file[name_column_name]

        return data_column, directory_name_column, name_column

    def _generate(self, data_piece, directory_name, name, index=None):
        code = qrcode.make(data_piece, box_size=2)
        path = os.path.join(self.outputs_directory, directory_name, f'{name}.png')
        code.save(path)


class ExcelImageQrCodeGenerator(ExcelQrCodeGenerator):

    def _generate(self, data_piece, directory_name, name, index):
        GTIN_column = self.file['GTIN']
        LOT_column = self.file['LOT']
        expire_date_column = self.file['ExpireDate']
        data = {
            'GTIN: ': str(GTIN_column[index]),
            'LOT: ': str(LOT_column[index]),
            'Expire Date: ': expire_date_column[index]
        }
        code_info = self.__generate_info_image(data)
        code = qrcode.make(data_piece, box_size=2)
        path = os.path.join(self.outputs_directory, directory_name, f'{name}.png')
        self.__generate_final_image(code, code_info, path)

    def __generate_info_image(self, data):
        generator = ImageGenerator()
        height = 5
        img = None
        for key, value in data.items():
            settings = {
                'size' : (140, 58),
                'font_file': './Aller_Bd.ttf',
                'font_size': 8,
                'text_position': (0, height),
                'image': img
            }
            img = generator.text_image(key, **settings)
            settings.update({
                'font_file': './Aller_Lt.ttf',
                'text_position': (45 if key == 'Expire Date: ' else 21, height),
                'image': img
            })
            img = generator.text_image(value, **settings)
            height += 15

        return img

    def __generate_final_image(self, code, code_info, path):
        generator = ImageGenerator()
        img = generator.merge(code, code_info, direction='horizontal')
        img.save(path)