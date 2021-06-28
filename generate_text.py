import tensorflow as tf
a = tf.constant(1.0)
b = tf.constant(2.0)
c = a + b
with tf.Session() as sess:
    print(sess.run(c))