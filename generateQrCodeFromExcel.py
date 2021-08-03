from qrCodeGenerator import ExcelQrCodeGenerator

import sys

def main():
    generator = ExcelQrCodeGenerator(filename=sys.argv[1])
    generator.set_directory_name_reference(sys.argv[2])
    generator.generate('UID', sys.argv[3])


if __name__ == "__main__":
    main()
