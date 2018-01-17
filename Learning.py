from keras.preprocessing import image
from keras.layers import Conv2D, Dense, Dropout, MaxPool2D, Flatten
from keras.models import Sequential
from keras.callbacks import TensorBoard
#preprocess all image in batch, This task is kind of CPU intensive, beginners, be aware!!

print('Processing...')


generator = image.ImageDataGenerator(rescale=1./255)

print('Preprocessing...')
datagen = generator.flow_from_directory(
    directory="Images/flower_photos",
    target_size=(40,40),
    save_prefix='1',
    save_to_dir='Image_gen/flower_photos'
)

def model():
    #Produces a simple, light weight CNN
    model = Sequential()
    model.add(Conv2D(
        filters=32, 
        kernel_initializer='glorot_uniform', 
        strides=(3, 3), 
        activation='relu',
        input_shape=(40,40,3),
        kernel_size=(3,3)
    ))
    model.add(Dropout(rate=0.2))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Flatten())

    #Densely connected deep network, to accept inputs from CNN
    model.add(Dense(units=512, activation='relu'))
    model.add(Dropout(rate=0.2))
    model.add(Dense(5, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

#create a TensorBoard callback to visualize Graph

tensor_callback = TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=True)

model = model()

model.fit_generator(
        generator=datagen,
        nb_epoch=40,
        samples_per_epoch=2000,
        nb_val_samples=800,
        callbacks = [tensor_callback]
    )
model.save(filepath='model.h5')
