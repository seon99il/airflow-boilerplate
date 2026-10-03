import os

from core.meta import get_name


def print_meta() -> None:
    print("data_interval_start:", os.environ["DATA_INTERVAL_START"])

    print("name: ", get_name())
    print("data_interval_end:", os.environ["DATA_INTERVAL_END"])


if __name__ == "__main__":
    os.environ["DATA_INTERVAL_START"] = "2023-01-01T00:00:00Z"
    os.environ["DATA_INTERVAL_END"] = "2023-01-02T00:00:00Z"
    print_meta()
