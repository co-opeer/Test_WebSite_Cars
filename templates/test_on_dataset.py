
import os
import tensorflow as tf


from keras_tuner.src.backend import keras

from templates.const import saved_model_path

model = keras.models.load_model(saved_model_path)


def predict_car(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array, verbose=0)
    return predictions[0] > 0.5


def test_model(directory_path):
    true_count = 0
    false_count = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            image_path = os.path.join(root, file)
            result = predict_car(image_path)


            if result:
                true_count += 1
            else:
                false_count += 1

    num_cars = len(os.listdir(directory_path))



    return num_cars, true_count, false_count



#a = test_model(r"C:\Users\PC\PycharmProjects\Test_WebSite_Cars\templates\photo")

