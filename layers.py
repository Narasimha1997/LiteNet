from keras.models import load_model


model = load_model('model.h5')

for layer in model.layers:
    print(layer.name)