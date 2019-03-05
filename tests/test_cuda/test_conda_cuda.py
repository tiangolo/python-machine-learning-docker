import docker
import pytest

from ..utils import CONTAINER_NAME, remove_previous_container

client = docker.from_env()


def verify_container(logs, python_version):
    assert "conda version: conda 4." in logs
    assert f"python version: {python_version}" in logs
    assert "NVIDIA-SMI" in logs
    assert "GPU Memory" in logs


@pytest.mark.parametrize(
    "image,python_version",
    [
        ("tiangolo/python-machine-learning:conda-cuda9.1-python3.6", "3.6"),
        ("tiangolo/python-machine-learning:conda-cuda9.1-python3.7", "3.7"),
    ],
)
def test_defaults(image, python_version):
    remove_previous_container(client)
    logs = client.containers.run(image, name=CONTAINER_NAME, remove=True)
    verify_container(logs.decode("utf-8"), python_version)
