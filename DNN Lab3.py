# Code by Krypto Kiddo
# Subject: DNN - Deep Neural Networks | Lab Assignment 03
# Aim: Understanding Data Pipelines in Tensorflow 2.0

# Reference and Guidance: https://www.tensorflow.org/datasets/keras_example
# Teacher's provided reference: https://medium.com/@karanaryan/a-beginners-guide-to-data-pipelines-in-tensorflow-2-0-a291535bd5c3

# IMPORTS
# Importing what's needed dude.
import tensorflow as tf
import tensorflow_datasets as tfds




# LOADING THE DATASET
# This is where we load the dataset. 
(ds_train, ds_test), ds_info = tfds.load(
    'mnist', # MNIST Dataset
    split=['train', 'test'], # Splitting dataset into training and testing bootstraps
    shuffle_files=True, # Randomly shuffling the files in dataset
    as_supervised=True, # Telling the program to treat the dataset as supervised
    with_info=True, # Telling the program that the dataset images contained info with them
)




# BUILDING A TRAINING PIPELINE

def normalize_img(image, label):
  """Normalizes images: `uint8` -> `float32`."""
  return tf.cast(image, tf.float32) / 255., label 

ds_train = ds_train.map(
    normalize_img, num_parallel_calls=tf.data.AUTOTUNE) # Normalising the input
ds_train = ds_train.cache() # Caching the data before shuffling for better perfomance as we fit it into memory 
ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples) #Shuffling happens here.
ds_train = ds_train.batch(128) # Batching the elements of the dataset to get unique batches at each epoch
ds_train = ds_train.prefetch(tf.data.AUTOTUNE) # Its usually good to end the pipeline by prefetching, or so I have read. 




# BUILDING A TESTING PIPELINE
# Its basically same as the training pipeline but there will be two differences:
# 1) We don't shuffle it
# 2) "Caching is done after batching because batches can be the same between epochs."
ds_test = ds_test.map(
    normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
ds_test = ds_test.batch(128)
ds_test = ds_test.cache()
ds_test = ds_test.prefetch(tf.data.AUTOTUNE)




# CREATE AND TRAIN THE MODEL
# Plug the TFDS input pipeline into a simple Keras model, compile the model, and train it.

# Creating the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10)
])

# This is where we compile it
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
)

# And this is where finally the fitting is done.
model.fit(
    ds_train,
    epochs=10,
    validation_data=ds_test,
)

# Voila and Ciao folks, cya again!
