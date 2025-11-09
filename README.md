# Airflow Boilerplate

> Airflow를 Docker-compose 환경에서 쉽게 시작할 수 있도록 도와주는 보일러플레이트입니다.

#### Features

- uv:  Local python package management
- CI: GitHub Actions를 이용한 pytest Base CI Environment
- Ansible: Ansible을 이용한 Docker Container `requirements.txt` Manual 동기화 스크립트
- ruff: 코드 스타일 자동화 도구(ruff)를 이용한 코드 스타일 검사


- `requirements-base.txt, requirements.txt` 파일을 분리하여 pip install 캐시 효과 극대화

_local 환경에서 Unit Test 시 Airflow DB 초기화가 필요할 수 있습니다 (`uv run airflow db init`)_
### Getting Started

```shell
git clone https://github.com/seon99il/airflow-boilerplate.git
brew install uv # for local python package management
uv sync

sh ./scripts/docker-compose-up.sh
```

#### Unit Test

```shell
$ uv run airflow db init # Local Airflow 환경이 필요할 수 있습니다.
$ uv run pytest -v
```

#### CI

```shell
brew install act # for local GitHub Actions testing
act -j ci-test
```

#### Ansible for Docker Container requirements.txt Manual Sync

```shell
sh ./scripts/sync-pip-from-reqs.sh
```

_scripts 안의 docker compose name 및 ansible hosts는 동일한 값이여야 함_