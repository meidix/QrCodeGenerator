import sys
import qrcode


def main():
    """
    generates a qr code based on the arguments it gets from the command line
    """
    img = qrcode.make(sys.argv[1], box_size=1)
    img.save(f"{sys.argv[2]}.png")


if __name__ == "__main__":
    main()
