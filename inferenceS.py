from keras.models import load_model
from PIL import Image
import numpy

label_dict = {
    '0' : 'daisy',
    '1' : 'dandelion',
    '2' : 'roses',
    '3' : 'sunflowers',
    '4' : 'tulips'
}

img = Image.open("dand.jpg")
img = img.resize((40,40))

image_array = numpy.array(img, dtype='float32')
image_array/=255
image_array = image_array.reshape((1,40,40,3))

LiteNet = load_model('model.h5')

predictions = LiteNet.predict(image_array)
label = label_dict[str(numpy.argmax(a = predictions))]
print(label)