# Code by Krypto Kiddo
# Subject: DNN - Deep Neural Networks | Lab Assignment 02
# Aim : Compute Y = WX+bWX+b where W, XW ,X , and b are drawn from a random normal distribution. W is of shape (4, 3), X is (3,1) and b is (4,1).


import tensorflow as tf  # Note: tf != thefuck!
import numpy as np

# THE BELOW REFERENCE CODE WAS OMITTED BECAUSE OF VERSION CAPABILTY ISSUES WITH GOOGLE COLAB'S INBUILT TENSORT FLOW LIBRARY

'''def linear_function():
  np.random.seed(1)
  ## CODE BEGINS ##
  X = tf.constant(np.random.randn(3,1),name="X")
  W = tf.constant(np.random.randn(4,3), name="W")
  b = tf.constant(np.random.randn(4,1), name="b")
  Y = tf.add(tf.matmul(W,X),b)

  sess = tf.compat.v1.Session()
  result = sess.run(Y)
  sess.close()
  return result

print("result = "+str(linear_function()))'''

with tf.compat.v1.Session() as sess:
  np.random.seed(1)
  # Build a dataflow graph.
  X = tf.constant(np.random.randn(3,1),name="X")
  W = tf.constant(np.random.randn(4,3), name="W")
  b = tf.constant(np.random.randn(4,1), name="b")
  Y = tf.add(tf.matmul(W,X),b)

  # Execute the graph and store the value that `Y` represents in `result`.
  result = sess.run(Y)
  
 # Print the result ofcourse.
 print(result)
  
