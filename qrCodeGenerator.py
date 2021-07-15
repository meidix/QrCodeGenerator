import qrcode
import sys
# img =  qrcode.make("Hello. I Am A QRCODE")
# img.save('qrcode.png')

def main():
    img = qrcode.make(sys.argv[1])
    img.save(f'{sys.argv[2]}.png')

if __name__ == '__main__':
    main()