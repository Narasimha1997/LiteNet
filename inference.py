from keras.models import load_model
from PIL import Image
import numpy
import os

label_dict = {
    '0' : 'daisy',
    '1' : 'dandelion',
    '2' : 'roses',
    '3' : 'sunflowers',
    '4' : 'tulips'
}

class_ = "roses"

LiteNet = load_model('model.h5')

def preprocessor(image_):
    img = Image.open('Images/flower_photos/'+class_+'/'+image_)
    img = img.resize((40,40))

    image_array = numpy.array(img, dtype='float32')
    image_array/=255
    return image_array.reshape((1,40,40,3))

count = 0
accurate = 0
for file_ in os.listdir('Images/flower_photos/'+class_):
    predictions = LiteNet.predict(preprocessor(file_))
    label = label_dict[str(numpy.argmax(a = predictions))]
    print(label)
    count+=1
    if label==class_:
        accurate+=1

print('Total images subjected for prediction: ', count)
print('Correct predictions: ', accurate)
print("results: ", (accurate/count)*100)