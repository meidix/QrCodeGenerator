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
