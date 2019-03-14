#! /usr/bin/env sh
set -e

echo "conda version: $(conda --version)"

python -c 'import sys; print("python version: {}.{}".format(sys.version_info.major, sys.version_info.minor))'

nvidia-smi
