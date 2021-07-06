import cv2
from PIL import Image, ImageDraw
from colorthief import ColorThief
import numpy as np


def color_detection(image, path):
    color_thief = ColorThief(image)
    # get the dominant color
    # dominant_color = color_thief.get_color(quality=2)
    palette = color_thief.get_palette(color_count=6)
    palette = np.array(palette)[np.newaxis, :, :]
    # print(dominant_color)
    # print(palette)

    # plt.imshow(palette)
    # plt.axis('off')
    # plt.show()
    # plt.savefig(palette)
    # cv2.imwrite(path, palette)

    width = len(palette[0]) * 50
    out = Image.new("RGB", (width, 50), (255, 255, 255))
    draw = ImageDraw.Draw(out)

    for idx, color in enumerate(palette[0]):
        start = 50 * idx
        end = 50 * (idx + 1)
        xy = [start, 0, end, 50]
        draw.rectangle(xy, fill=tuple(color), )

    out.save(path)
    # return np.asarray(Image.open(path).convert("RGB"))
    # return Image.fromarray(palette, 'RGBA')
    return path
