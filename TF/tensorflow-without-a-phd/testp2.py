import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases  = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function:
        outputs = activation_function(Wx_plus_b)
    else:
        outputs = Wx_plus_b
    return outputs

x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise  = np.random.normal(0, 0.05, x_data.shape) # normal distribution
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32, [None, 1.0])
ys = tf.placeholder(tf.float32, [None, 1.0])

l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()


sess = tf.Session()
sess.run(init)

plt.close()
fig = plt.figure()

ax = fig.add_subplot(1,1,1)
plt.ion() # for dynamicly update plot, plt.show(block=False) in old version

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys:y_data})
    if i % 100 == 0:
        #print(sess.run(loss, feed_dict={xs: x_data, ys:y_data}))
        try:
            print("hi")
            #ax.lines.remove(lines[0]) # remove last line
            ax.lines.pop()
        except Exception:
            print("ho")
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)
