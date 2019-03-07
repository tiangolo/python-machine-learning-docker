[![Build Status](https://travis-ci.org/tiangolo/python-machine-learning-docker.svg?branch=master)](https://travis-ci.org/tiangolo/python-machine-learning-docker)


## Supported tags and respective `Dockerfile` links

* [`python3.7`, `latest` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/python3.7/Dockerfile)
* [`python3.6` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/python3.6/Dockerfile)
* [`cuda9.1-python3.7` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/cuda9.1-python3.7/Dockerfile)
* [`cuda9.1-python3.6` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/cuda9.1-python3.6/Dockerfile)
* [`python3.6-tensorflow` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/python3.6-tensorflow/Dockerfile)
* [`cuda9.1-python3.6-tensorflow` _(Dockerfile)_](https://github.com/tiangolo/python-machine-learning-docker/blob/master/cuda9.1-python3.6-tensorflow/Dockerfile)


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
FROM tiangolo/python-machine-learning:python3.7

COPY ./main.py /app/main.py
```

or any of the image variants, e.g.:

```Dockerfile
FROM tiangolo/python-machine-learning:cuda9.1-python3.6-tensorflow

COPY ./main.py /app/main.py
```

By default it just checks and prints the versions of the software installed, Conda and Python. Also Nvida GPU and TensorFlow, in their respective image versions (tags).

You can override that behavior and run your own program creating a file at `/start.sh`.

For example:

```Dockerfile
FROM tiangolo/python-machine-learning:python3.7

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./main.py /app/main.py
```

**Note**: As the default command (`CMD`) is to run `/start.sh`, if you provide/overwrite that file, you don't have to add a `CMD /start.sh` in your `Dockerfile`.

## CUDA Technical details

First, to be able to run the CUDA versions with Docker you need to be on Linux, have Docker and an Nvidia GPU.

Then, there are compatibility requirements between versions.

### CUDA, GPU Driver, Nvidia Model

**CUDA** has to be a version that is compatible with the **Nvidia GPU driver**, which is compatible with a **GPU architecture** (a series of specific GPU models). The CUDA versions require Nvidia GPU driver versions "superior to" some driver number (they are backward compatible).

You can see the [compatibility table](https://github.com/NVIDIA/nvidia-docker/wiki/CUDA#requirements) at the **nvidia-docker** site.

### GPU Driver availability in Linux

As of 2019-03-06, the latest Nvidia driver for Linux is `418`, you can check in the [Nvidia Unix Drivers page](https://www.nvidia.com/object/unix.html).

But the latest driver officially available for Ubuntu is `390`, check in the [Ubuntu Nvidia drivers page](https://help.ubuntu.com/community/BinaryDriverHowto/Nvidia).

#### GPU Beta Drivers

There is a more technical option to install beta drivers.

You can [add the PPA (Personal Package Archive) for the user `~graphics-drivers`](https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa) and then you can install (as of 2019-03-06) up to version `410`.

### TensorFlow

**TensorFlow** versions are compatible with specific versions of **CUDA**.

There doesn't seem to be a single page specifying which versions of TensorFlow are compatible with which versions of CUDA, apart from the [GitHub releases page](https://github.com/tensorflow/tensorflow/releases).

The latest requirements (including CUDA version) (for the latest version of TensorFlow) can be found at the [GPU support section](https://www.tensorflow.org/install/gpu) in the official docs.

### Conda

**Conda** has TensorFlow pre-compiled (with the optimizations) in specific versions, compiled with specific versions of **CUDA**.

You can install TensorFlow with a specific CUDA version with, e.g.:

```bash
conda install tensorflow-gpu cudatoolkit=9.0
```

that will install TensorFlow compiled with GPU support (with CUDA) using a CUDA version of 9.0.

To see the available `cudatoolkit` versions in `conda`, you can run:

```bash
conda search cudatoolkit
```

### Current state

As of 2019-03-06, as the latest Nvidia driver officially [available for Ubuntu is `390`](https://help.ubuntu.com/community/BinaryDriverHowto/Nvidia), this limits the [compatible version of CUDA to max `9.1`](https://github.com/NVIDIA/nvidia-docker/wiki/CUDA#requirements) (unless using the beta drivers).

That's why the current CUDA flavor is version `9.1`. Even though there are superior base image versions, but those wouldn't run on an Ubuntu machine unless using the beta drivers (or drivers installed by hand, directly from the Nvidia site).

Then, Conda has `cudatoolkit` available in several versions, the latest are `9.0`, `9.2` and `10.0`. But as the base image is `9.1`, the latest version that is still compatible is `9.0`. That's the version used in the image tag with TensorFlow and CUDA. But as they are backward compatible, it works.

### Decide your versions

**Note**: this will apply when this image has more CUDA versions (tags). As of now, it only describes the process to decide versions and build this image.

First, check what is the architecture of your GPU, then what is the most recent driver you can install (deciding if you want to have beta drivers).

This applies for local development or cloud (if you use a cloud server with GPU).

Then, see what is the latest CUDA version you can have with that driver.

Then you can get the latest tag (version) of this image that is less than or equal to your driver.

Next, find which versions of `cudatoolkit` (CUDA) are available in `conda`. Choose the latest one that is less than or equal to the image you chose.

Then you can install TensorFlow with that `cudatoolkit`.

## Tests

All the image tags are tested.

CUDA (GPU usage) is tested locally (as CI systems don't provide GPUs easily).

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

You can also run the CUDA (GPU) tests:

```bash
bash scripts/test-cuda.sh
```

## Release Notes

### 0.2.0

* Refactor image tags, remove `conda-` prefix to all images to simplify. PR <a href="https://github.com/tiangolo/python-machine-learning-docker/pull/1" target="_blank">#1</a>.

### 0.1.0

* First release, including Conda, Python 3.7, Python 3.6, CUDA and TensorFlow.

## License

This project is licensed under the terms of the MIT license.
