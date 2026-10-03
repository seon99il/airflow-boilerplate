from airflow.providers.docker.operators.docker import DockerOperator

DEFAULT_IMAGE = "airflow-boilerplate/worker-default:{{ var.value.get('worker_image_tag', 'dev') }}"
SRC_DIR = "/app/src"


def _command(script: str, fn_name: str | None) -> list[str]:
    path = script.strip("/")
    if not path.endswith(".py") or ".." in path.split("/"):
        raise ValueError(f"script must be a .py path under {SRC_DIR}: {script!r}")
    if fn_name is None:
        return ["python", f"{SRC_DIR}/{path}"]
    module = path.removesuffix(".py").replace("/", ".")
    if not all(part.isidentifier() for part in module.split(".")):
        raise ValueError(f"script path is not importable: {script!r}")
    if not fn_name.isidentifier():
        raise ValueError(f"fn_name must be an identifier: {fn_name!r}")
    return ["python", "-c", f"from {module} import {fn_name}; {fn_name}()"]


class DomainDockerOperator(DockerOperator):

    def __init__(
            self,
            *,
            script: str,
            fn_name: str | None = None,
            image: str = DEFAULT_IMAGE,
            docker_url="unix://var/run/docker.sock",
            environment: dict[str, str] | None = None,
            **kwargs,
    ):
        environment = {
            "DATA_INTERVAL_START": "{{ data_interval_start }}",
            "DATA_INTERVAL_END": "{{ data_interval_end }}",
            **(environment or {}),
        }
        super().__init__(
            image=image,
            container_name="{{ task_instance.task_id }}_{{ ts_nodash }}",
            command=_command(script, fn_name),
            docker_url=docker_url,
            environment=environment,
            **kwargs,
        )
