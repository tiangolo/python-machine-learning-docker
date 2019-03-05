import os
import time

import docker
import pytest

from ..utils import CONTAINER_NAME, get_logs, remove_previous_container

TEST_GPU = os.getenv("TEST_GPU")

client = docker.from_env()


def verify_container(container, python_version):
    logs = get_logs(container)
    assert "conda version: conda 4." in logs
    assert f"python version: {python_version}" in logs
    if TEST_GPU:
        assert f"NVIDIA-SMI" in logs
        assert f"GPU Memory" in logs


@pytest.mark.parametrize(
    "image,python_version",
    [
        ("tiangolo/python-machine-learning:conda-cuda9.1-python3.6", "3.6"),
        ("tiangolo/python-machine-learning:conda-cuda9.1-python3.7", "3.7"),
    ],
)
def test_defaults(image, python_version):
    remove_previous_container(client)
    container = client.containers.run(image, name=CONTAINER_NAME, detach=True)
    time.sleep(1)
    verify_container(container, python_version)
    container.stop()
    container.remove()
