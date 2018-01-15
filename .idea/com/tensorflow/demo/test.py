import tensorflow as tf


input = tf.Variable(tf.random_normal([1,3,3,5]))
filter = tf.Variable(tf.random_normal([1,1,5,1]))
op = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='VALID')

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
print(input.eval())
print(filter.eval())
print(op.eval())