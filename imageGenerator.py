from PIL import Image, ImageDraw, ImageFont


class ImageGenerator:

    def text_image(self, text, **kwargs):
        mode = kwargs.setdefault('mode', 'RGB')
        size = kwargs.setdefault('size', (150, 50))
        color = kwargs.setdefault('color', '#FFFFFF')
        font_file = kwargs.setdefault('font_file', None)
        font_size = kwargs.setdefault('font_size', 14)
        text_position = kwargs.setdefault('text_position', (50, 15))
        fill = kwargs.setdefault('fill', '#000000')
        image = kwargs.setdefault('image', None)

        if font_file:
            font = ImageFont.truetype(font_file, size=font_size)
        else:
            font = ImageFont.load_default()

        if image:
            img = image.copy()
        else:
            img = Image.new(mode=mode, size=size, color=color)

        canvas = ImageDraw.Draw(img)
        canvas.text(text_position, text, font=font, fill=fill)

        return img

    def merge(self, *args, direction='vertical', mode='RGB', color='#FFFFFF'):
        '''
        Takes a number of images and depending on the direction merges them togather
        '''
        args = list(args)
        if len(args) == 0:
            raise Exception('No Image is set')

        width, height = args[0].size

        # check if images are mergable
        for image in args:
            w, h = image.size
            if not h == height and direction == 'horizontal':
                raise Exception("images are not the same height")
            elif not w == width and direction == 'vertical':
                raise Exception("images not the same width")

        positions = []
        if direction == 'horizontal':
            img_width = 0
            for image in args:
                img_width += image.width

            img_height = height
            for i in range(len(args)):
                positions.append((width*i, 0))

        elif direction == 'vertical':
            img_width = width
            img_height = 0
            for image in args:
                img_height += image.height
            for i in range(len(args)):
                positions.append((0, height*i))

        # actual merging
        result = Image.new(mode=mode, size=(img_width, img_height), color=color)
        for i in range(len(args)):
            result.paste(args[i], positions[i])

        return result

    def open(self, filename):
        img = Image.open(filename)
        resulting_image = Image.new(mode='RGB', size=img.size, color="#FFFFFF")
        resulting_image.paste(img, (0,0))
        return resulting_image
