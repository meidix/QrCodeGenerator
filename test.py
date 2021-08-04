from qrCodeGenerator import ExcelQrCodeGenerator
from imageGenerator import ImageGenerator

import pandas as pd
from PIL import Image

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

    def test_generationIsDoneCorrectly(self, *args, **kwargs):
        self.generator.set_directory_name_reference('Name')
        self.generator.generate('UID', name_column_name="Serial")


class ImageGeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.generator = ImageGenerator()

    def test_text_image_is_being_created(self, *args, **kwargs):
        image = self.generator.text_image("Hello World!", font_file="./Aller_Lt.ttf", font_size=16)

    def test_if_text_can_be_added_to_image(self, *args, **kwargs):
        image = self.generator.text_image("Hello World!", font_file="./Aller_Lt.ttf", font_size=14)
        new_imge = self.generator.text_image("GTIN:", font_file="./Aller_Bd.ttf", font_size=14, text_position=(10, 15), image=image)

    def test_if_the_images_are_merged_horizontaly_successfuly(self, *args, **kwargs):
        first_image = self.generator.open('right_qr.png')
        second_image = self.generator.text_image(
            "GTIN",
            size=(160, 58),
            font_file="./Aller_Bd.ttf",
            font_size=10,
            text_position=(10, 15)
        )
        final_img = self.generator.merge(first_image, second_image, direction="horizontal")
        width = first_image.width + second_image.width
        height = first_image.height
        self.assertEqual(final_img.size, (width, height))
        final_img.save('res1.png')

    def test_if_the_are_merged_verticaly_succesfully(self, *args, **kwargs):
        first_image = self.generator.text_image(
            "GTIN",
            size=(160, 15),
            font_file="./Aller_Bd.ttf",
            font_size=10,
            text_position=(10, 0)
        )
        first_image = self.generator.text_image(
            "06268176200271",
            size=(160, 15),
            image=first_image,
            font_file="./Aller_Lt.ttf",
            font_size=10,
            text_position=(35, 0)
        )
        second_image = self.generator.text_image(
            "LOT",
            size=(160, 15),
            font_file="./Aller_Bd.ttf",
            font_size=10,
            text_position=(10, 0)
        )
        second_image = self.generator.text_image(
            "00030101",
            size=(160, 15),
            image=second_image,
            font_file="./Aller_Lt.ttf",
            font_size=10,
            text_position=(35, 0)
        )
        third_image = self.generator.text_image(
            "IRC",
            size=(160, 15),
            font_file="./Aller_Bd.ttf",
            font_size=10,
            text_position=(10, 0)
        )
        third_image = self.generator.text_image(
            "5501520854101822",
            size=(160, 15),
            image=third_image,
            font_file="./Aller_Lt.ttf",
            font_size=10,
            text_position=(35, 0)
        )
        final_img = self.generator.merge(first_image, second_image, third_image)
        width = third_image.width
        height = first_image.height + second_image.height + third_image.height
        self.assertEqual(final_img.size, (width, height))
        final_img.save('res2.png')





if __name__ == "__main__":
    unittest.main()