#! /usr/bin/env sh
set -e

echo "conda version: $(conda --version)"

python -c 'import sys; print("python version: {}.{}".format(sys.version_info.major, sys.version_info.minor))'

python -c "import tensorflow as tf; print('tensorflow version: ' + str(tf.__version__))"

python -c "import tensorflow as tf; tf.enable_eager_execution(); print('tensorflow compute: ' + str(tf.reduce_sum(tf.random_normal([1000, 1000]))))"
