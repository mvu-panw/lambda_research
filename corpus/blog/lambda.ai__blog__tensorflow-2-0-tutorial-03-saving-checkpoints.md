# TensorFlow 2.0 Tutorial 03: Saving Checkpoints

Source: https://lambda.ai/blog/tensorflow-2-0-tutorial-03-saving-checkpoints

Skip to main content

# TensorFlow 2.0 Tutorial 03: Saving Checkpoints

 June 6, 2019

 (Updated on July 24, 2023)

 • 3 min read

This tutorial combines two items from previous tutorials: saving models and callbacks. Checkpoints are saved model states that occur during training. With TensorFlow 2, you'll implement a callback that repeatedly saves the model during training.

TensorFlow 2 offers Keras as its high-level API. As we have seen in the previous tutorial, Keras uses the Model.fit function to execute the training and hides the internal training loop from end users. The way to customize the training after each epoch has to be done via callback functions. In previous tutorials, we've already seen how to customize the learning rate, and how to log statistics using the LearningRateScheduler and TensorBoard callbacks.

In this tutorial, we will get to know the ModelCheckpoint callback. Use this repo to reproduce the results in this tutorial.

First, we define the path where we will save the checkpoints:

outputFolder = './output'
if not os.path.exists(outputFolder):
 os.makedirs(outputFolder)
filepath=outputFolder+"/model-{epoch:02d}-{val_accuracy:.2f}.hdf5"

The above code creates the output folder in the current directory to save the checkpoints. We also add the epoch and validation accuracy to the checkpoint name.

Next, we create the callback function:

checkpoint_callback = ModelCheckpoint(
 filepath, monitor='val_accuracy', verbose=1,
 save_best_only=False, save_weights_only=False,
 save_frequency=1)

The filepath defines the directory to save the checkpoints. monitor defines the variable to monitor which can be used in the filepath template string. One can use save_best_only to only save models which outperform previous ones based on the monitored variable. save_weights_only is used to discard the network topology in the checkpoint. Setting save_weights_only to True essentially calls model.save_weights; Setting it to False essentially calls model.save. In this example, we save both the model topology and weights. Last but not least, we use save_frequency to control how often do we write the checkpoint. Setting it to one means that you'll write a checkpoint out at each epoch. Use a larger number to write checkpoints less frequently.

Next, we attach the callback to the model.fit function. Notice, model validation is necessary because we need the val_accuracy value which is used in the checkpoint filepath. Also note, the validation_freq has to be synchronized with the save_frequency.

model.fit(train_dataset,
 epochs=3, callbacks=[checkpoint_callback],
 validation_data=test_dataset,
 validation_freq=1)

The above call will train the model for three epochs and create three checkpoints:

Epoch 1/3
390/390 [============================>.] - ETA: 0s - loss: 2.7178 - accuracy: 0.3176
Epoch 00001: saving model to ./output-cifar/model-01-0.18.hdf5
390/390 [==============================] - 73s 186ms/step - loss: 2.7175 - accuracy: 0.3176 - val_loss: 5.9952 - val_accuracy: 0.1824
Epoch 2/3
389/390 [============================>.] - ETA: 0s - loss: 2.2501 - accuracy: 0.4752 
Epoch 00002: saving model to ./output-cifar/model-02-0.41.hdf5
390/390 [==============================] - 39s 101ms/step - loss: 2.2505 - accuracy: 0.4751 - val_loss: 2.4505 - val_accuracy: 0.4075
Epoch 3/3
390/390 [==============================] - 40s 102ms/step - loss: 2.0264 - accuracy: 0.5594 - val_loss: 2.3908 - val_accuracy: 0.4931
Epoch 00003: saving model to ./output-cifar/model-03-0.49.hdf5

Now, let's resume the training from the second epoch. Notice the initial_epoch argument is the epoch index of the restored model. Thus the training will begin at initial_epoch + 1.

model_info = model.fit(train_dataset,
 epochs=5, callbacks=[checkpoint_callback],
 validation_data=test_dataset,
 validation_freq=1,
 initial_epoch = 1)

Epoch 2/5
390/390 [==============================] - 39s 101ms/step - loss: 1.8649 - accuracy: 0.6138 - val_loss: 2.6372 - val_accuracy: 0.4056
Epoch 00002: saving model to ./output-cifar/model-02-0.41.hdf5
Epoch 3/5
390/390 [==============================] - 40s 102ms/step - loss: 1.7176 - accuracy: 0.6642 - val_loss: 2.2977 - val_accuracy: 0.5040
Epoch 00003: saving model to ./output-cifar/model-03-0.50.hdf5
Epoch 4/5
390/390 [==============================] - 40s 102ms/step - loss: 1.6002 - accuracy: 0.7010 - val_loss: 1.8743 - val_accuracy: 0.6202 
Epoch 00004: saving model to ./output-cifar/model-04-0.62.hdf5
Epoch 5/5
390/390 [==============================] - 40s 101ms/step - loss: 1.5031 - accuracy: 0.7292 - val_loss: 1.9608 - val_accuracy: 0.5892
Epoch 00005: saving model to ./output-cifar/model-05-0.59.hdf5

## Summary

This tutorial explained how to use checkpoints to save and restore TensorFlow models during the training. The key is to use tf.keras.ModelCheckpoint callbacks to save the model. Set initial_epoch in the model.fit call to restore the model from a pre-saved checkpoint.

All code from this tutorial series can be found in this repo.

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
