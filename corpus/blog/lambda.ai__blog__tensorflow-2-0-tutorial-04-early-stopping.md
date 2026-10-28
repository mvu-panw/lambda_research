# TensorFlow 2.0 Tutorial 04: Early Stopping

Source: https://lambda.ai/blog/tensorflow-2-0-tutorial-04-early-stopping

Skip to main content

# TensorFlow 2.0 Tutorial 04: Early Stopping

 June 6, 2019

 (Updated on July 24, 2023)

 • 2 min read

During training, weights in the neural networks are updated so that the model performs better on the training data. For a while, improvements on the training set correlate positively with improvements on the test set. However, there comes a point where you begin to overfit on the training data and further "improvements" will result in lower generalization performance. This is known as overfitting. Early stopping is a technique used to terminate the training before overfitting occurs.

This tutorial explains how early stopping is implemented in TensorFlow 2. All code for this tutorial is available in our repository.

Early stopping is implemented in TensorFlow via the tf.keras.EarlyStopping callback function:

earlystop_callback = EarlyStopping(
 monitor='val_accuracy', min_delta=0.0001,
 patience=1)

monitor keep track of the quantity that is used to decide if the training should be terminated. In this case, we use the validation accuracy. min_delta is the threshold that triggers the termination. In this case, we require that the accuracy should at least improve 0.0001. patience is the number of "no improvement epochs" to wait until training is stopped. With patience = 1, training terminates immediately after the first epoch with no improvement.

Now, we can attach the early stop callback and run training with early stopping:

model.fit(train_dataset,
 epochs=10, callbacks=[earlystop_callback],
 validation_data=test_dataset,
 validation_freq=1)

Epoch 1/10
390/390 [==============================] - 73s 187ms/step - loss: 2.7133 - accuracy: 0.3300 - val_loss: 6.3186 - val_accuracy: 0.1752
Epoch 2/10
390/390 [==============================] - 39s 100ms/step - loss: 2.2262 - accuracy: 0.4914 - val_loss: 2.5499 - val_accuracy: 0.4358
Epoch 3/10
390/390 [==============================] - 39s 100ms/step - loss: 1.9842 - accuracy: 0.5801 - val_loss: 2.5666 - val_accuracy: 0.4708
Epoch 4/10
390/390 [==============================] - 39s 99ms/step - loss: 1.8144 - accuracy: 0.6333 - val_loss: 2.2643 - val_accuracy: 0.5407
Epoch 5/10
390/390 [==============================] - 39s 99ms/step - loss: 1.6799 - accuracy: 0.6770 - val_loss: 2.1015 - val_accuracy: 0.5841
Epoch 6/10
390/390 [==============================] - 39s 99ms/step - loss: 1.5700 - accuracy: 0.7104 - val_loss: 2.0468 - val_accuracy: 0.6078
Epoch 7/10
390/390 [==============================] - 38s 98ms/step - loss: 1.4697 - accuracy: 0.7388 - val_loss: 2.0628 - val_accuracy: 0.5925
Epoch 00007: early stopping

Notice the 7th epoch resulted in better training accuracy but lower validation accuracy. Thus, the training terminated at the 7th epoch despite the fact that the maximum number of epochs is set to 10.

## Summary

This tutorial explains how early stopping is implemented in TensorFlow 2. The key takeaway is to use the tf.keras.EarlyStopping callback. Early stopping is triggered by monitoring if a certain value (for example, validation accuracy) has improved over the latest period of time (controlled by the patience argument).

To reproduce these results, please refer to this code repo.

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
