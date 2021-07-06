from PIL import Image, ImageDraw


def symmetry_detection(img_path, save_path):
    out = Image.open(img_path)
    draw = ImageDraw.Draw(out)
    draw.line((0, 0) + out.size, fill=128)
    draw.line(out.size + (0, 0), fill=(255, 255, 0))
    out.save(save_path)
    return save_path
