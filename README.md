[![Build Status](https://travis-ci.org/tiangolo/python-machine-learning-docker.svg?branch=master)](https://travis-ci.org/tiangolo/python-machine-learning-docker)


## Supported tags and respective `Dockerfile` links

* [`conda-python3.7`, `latest` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/conda-python3.7/Dockerfile)
* [`conda-python3.6` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/conda-python3.6/Dockerfile)
* [`conda-cuda9.1-python3.7` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/conda-cuda9.1-python3.7/Dockerfile)
* [`conda-cuda9.1-python3.6` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/conda-cuda9.1-python3.6/Dockerfile)
* [`conda-python3.6-tensorflow` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/conda-python3.6-tensorflow/Dockerfile)
* [`conda-cuda9.1-python3.6-tensorflow` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/conda-cuda9.1-python3.6-tensorflow/Dockerfile)


# python-machine-learning

[**Docker**](https://www.docker.com/) image with **[Python](https://www.python.org/) 3.7** and **3.6** for Machine Learning.

Uses [**Conda**](https://conda.io/en/latest/) (installed with [Miniconda](https://docs.conda.io/en/latest/miniconda.html)).

Includes optional variants with [**Nvidia CUDA**](https://www.geforce.com/hardware/technology/cuda).

**GitHub repo**: <https://github.com/tiangolo/python-machine-learning-docker>

**Docker Hub image**: <https://hub.docker.com/r/tiangolo/python-machine-learning>

## Description

This Docker image is made to serve as a base for other images and projects for Machine Learning, Data Science, Deep Learning, etc.

It does not try to include every possible package. On the contrary, it tries to be as slim as possible, but having the minimal common requirements (the difficult parts) for most projects.

By being slim, apart from reducing the size, it can be kept current more easily, and it can be tailored for each project, being equally useful for development and production.

### Conda

It includes [**Conda**](https://conda.io/en/latest/) (Miniconda, the package manager from Anaconda).

Conda is, more or less, the "de-facto" standard package manager for Machine Learning Python projects (Data Science, Deep Learning, etc).

With it, you can install most of the packages used in Machine Learning with a simple command.

For example, to install Pandas, you can run:

```bash
conda install pandas
```

In a `Dockerfile` you would add that with:

```Dockerfile
RUN conda install -y pandas
```

`conda` is especially useful for Machine Learning and Data Science (compared to other package managers like `pip`, `pipenv`) because in many cases it installs optimized versions, compiled with **Intel MKL** (which is not available via `pip`).

For example, TensorFlow is compiled with [**Intel MKL-DNN**](https://www.anaconda.com/tensorflow-in-anaconda/), which gives up to 8x the performance achievable with `pip`.

### Nvidia CUDA

[**Nvidia CUDA**](https://www.geforce.com/hardware/technology/cuda) is needed to be able to use the GPU, mainly for Deep Learning. There are optional image versions (tags) including CUDA.

For these versions to work, you need to have an Nvidia GPU and have [**nvidia-docker**](https://github.com/NVIDIA/nvidia-docker) installed.

**nvidia-docker** is in many cases easier to install and use than installing the full set of dependencies (CUDA, CuDNN, etc) in your local machine.

This is especially true when you have more than one project, with different dependencies/versions.

### TensorFlow

[**TensorFlow**](https://www.tensorflow.org/) is Google's very popular Deep Learning framework.

There are versions (tags) of this image with **TensorFlow** already installed with `conda` (with its performance gains). Contrary to the official TensorFlow Docker images, that are installed with `pip`.

There are also versions with TensorFlow and CUDA. So, you can run TensorFlow (built with the `conda` optimizations) on your GPU, from Docker.

## How to use

* You don't need to clone the GitHub repo. You can use this image as a base image for other images, using this in your `Dockerfile`:

```Dockerfile
FROM tiangolo/python-machine-learning:conda-python3.7

COPY ./main.py /app/main.py
```

or any of the image variants, e.g.:

```Dockerfile
FROM tiangolo/python-machine-learning:conda-cuda9.1-python3.6-tensorflow

COPY ./main.py /app/main.py
```

By default it just checks and prints the versions of the software installed, Conda and Python. Also Nvida GPU and TensorFlow, in their respective image versions (tags).

You can override that behavior and run your own program creating a file at `/start.sh`.

For example:

```Dockerfile
FROM tiangolo/python-machine-learning:conda-python3.7

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./main.py /app/main.py
```

**Note**: As the default command (`CMD`) is to run `/start.sh`, if you provide/overwrite that file, you don't have to add a `CMD /start.sh` in your `Dockerfile`.

## Tests

All the image tags are tested.

GPU usage is tested locally (as CI system don't provide GPUs easily).

To run the tests, you need to have the [`Docker SDK for Python`](https://docker-py.readthedocs.io/en/stable/index.html) installed.

If you are using Pipenv locally, you can install the development dependencies with:

```bash
pipenv shell
pipenv install --dev
```

Then you can run the tests locally:

```bash
bash scripts/test.sh
```

And you can enable GPU testing while running the tests:

```bash
TEST_GPU=1 bash scripts/test.sh
```

## Release Notes

### 0.1.0

* First release, including Conda, Python 3.7, Python 3.6, CUDA and TensorFlow.


## License

This project is licensed under the terms of the MIT license.
