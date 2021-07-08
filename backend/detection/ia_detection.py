import numpy as np
from tensorflow.keras.preprocessing import image

from detection import get_model


def ia_detection(tst_src):
    model = get_model()
    # model.summary()

    # model = load_model('ia/')
    # tst_src = 'imgs/melanoma.jpeg'
    test_melanoma_img = image.load_img(tst_src, target_size=(224, 224, 3))

    # plt.imshow(test_melanoma_img)
    # plt.show()

    test_melanoma_img_array = image.img_to_array(test_melanoma_img, )
    test_melanoma_img_batch = np.expand_dims(test_melanoma_img_array / 255.0, axis=0, )

    # x = img_to_array(img)
    # x = x/255

    # model.p
    prediction = model.predict(test_melanoma_img_batch, verbose=0)
    print(prediction)
    percentage = (prediction[0][0] * 100)
    print("Melanoma?: {:.2f}%".format(percentage))
    return percentage

# ia_detection()
