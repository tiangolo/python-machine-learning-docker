from docker.errors import NotFound

CONTAINER_NAME = "python-machine-learning-testconctainer"
IMAGE_NAME = "python-machine-learning-testimage"


def remove_previous_container(client):
    try:
        previous = client.containers.get(CONTAINER_NAME)
        previous.stop()
        previous.remove()
    except NotFound:
        return None


def get_logs(container):
    logs: str = container.logs()
    return logs.decode("utf-8")
