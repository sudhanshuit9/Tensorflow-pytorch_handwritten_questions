#Write a 2D tensor of shape (3,3) with randvalue  between 0 & 1

import tensorflow as tf
tensor = tf.random.uniform((3,3),minval=0, maxval=1)
print(tensor)