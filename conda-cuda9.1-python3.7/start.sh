#! /usr/bin/env sh
set -e

echo "conda version: $(conda --version)"

echo "python version: $(python -c 'import sys; print("{}.{}".format(sys.version_info.major, sys.version_info.minor))')"

nvidia-smi
