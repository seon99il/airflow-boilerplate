# Airflow Boilerplate

> Airflow를 Docker-compose 환경에서 쉽게 시작할 수 있도록 도와주는 보일러플레이트입니다.

#### Features

- uv:  Local python package management
- CI: GitHub Actions를 이용한 pytest Base CI Environment
- Ansible: Ansible을 이용한 Docker Container `requirements.txt` Manual 동기화 스크립트

### Getting Started

```shell
git clone https://github.com/seon99il/airflow-boilerplate.git
brew install uv # for local python package management
uv sync

sh ./scripts/docker-compose-up.sh
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