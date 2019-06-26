from PIL import Image


def to_bw(image_path, output_path):
    """Converts image to binary black and white"""
    image_file = Image.open(image_path)
    threshold = 128
    image_file = image_file.point(lut=lambda p: p > threshold and 255)
    image_file = image_file.convert('1', dither=Image.FLOYDSTEINBERG )
    image_file.save(output_path)
