import base64
import io

from sqlalchemy.orm.collections import InstrumentedList
from PIL import Image


def serialize(item):
    return item.serialize


def to_json(lst):
    if type(lst) is list or type(lst) is InstrumentedList:
        return list(map(serialize, lst))
    else:
        return lst.serialize


def image_to_base64(filename):
    with Image.open(filename) as image_file:
        buffer = io.BytesIO()
        image_file.save(buffer, format='PNG')
        buffer.seek(0)
        img = buffer.read()
        b64 = base64.b64encode(img).decode('ascii')
        return 'data:image/png;base64,{0}'.format(b64), filename
