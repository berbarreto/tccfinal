from keras.models import load_model

KERAS_MODEL = None


def set_model():
    global KERAS_MODEL
    KERAS_MODEL = load_model('ia/')


def get_model():
    return KERAS_MODEL
