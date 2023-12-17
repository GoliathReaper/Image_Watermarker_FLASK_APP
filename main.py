from PIL import Image, ImageDraw, ImageFont


def image_watermarker(water_mark_text, img, opacity):
    # get an image
    with Image.open(img).convert("RGBA") as base:

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        width, height = base.size

        # get a font
        # fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        for i in range(1, width, 100):
            for j in range(1, height, 100):
                print(i, j)
                d.text((i, j), water_mark_text, fill=(255, 255, 255, opacity))
                # default opacity d.text((i, j), water_mark_text, fill=(255, 255, 255, 128))

        # # draw text, full opacity
        # d.text((10, 60), "World", fill=(255, 255, 255, 255))

        out = Image.alpha_composite(base, txt)

        out.show()

# todo: add space or density of watermark
# todo: add font type
# todo: add gui using tkinter
# todo: Web application using flask
# todo: user can change the color of text
# todo: user can change the position of the copyright text, either text fill entire image with user defined space or user define the position of the text
