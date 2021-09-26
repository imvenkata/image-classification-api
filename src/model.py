

from io import BytesIO
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications import imagenet_utils


model = None


# Load the pre-trained Keras model (here we are using a model
# pre-trained on ImageNet and provided by Keras, but you can
# substitute in your own networks just as easily)

class imageClassifier:

    def __init__(self):
        self.model = tf.keras.applications.densenet.DenseNet121(weights="imagenet")
        print("Model loaded")
    
    # read image
    def read_image(self, image_encoded):
        pil_image = Image.open(BytesIO(image_encoded))
        return pil_image

    #image pre-processing
    def preprocess(self, image: Image.Image):
        image = image.resize((224, 224))
        image = np.asarray(image)[..., :3]
        image = np.expand_dims(image, 0)
        image = image / 127.5 - 1.0
        return image

    #final prediction
    def predict(self, image : np.ndarray):
        prediction = self.model.predict(image)
        prediction = imagenet_utils.decode_predictions(prediction)[0][0][1]
        return prediction

    