# Airflow Boilerplate

> Airflow를 Docker-compose 환경에서 쉽게 시작할 수 있도록 도와주는 보일러플레이트입니다.

#### Features

- uv:  Local python package management
- CI: GitHub Actions를 이용한 pytest Base CI Environment
- Ansible: Ansible을 이용한 Docker Container `requirements.txt` Manual 동기화 스크립트
- ruff: 코드 스타일 자동화 도구(ruff)를 이용한 코드 스타일 검사
- custom-libs: custom lib(component)를 구성하고 CI, Docker Airflow 환경에 자동으로 반영 적용


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

#### custom components

> src/lib 안에 코드를 구성하여 Import 시 path 최적화

- Docker image 빌드 시 src/lib/install_lib.sh 스크립트를 통해 lib 디렉토리 내 라이브러리 목록을 설치
- Docker compose 환경에서 volume 마운트로 코드 변경 자동 반영
- pyproject.toml를 활용한 uv add lib-a 명령어로 local 환경에 lib-a 패키지 설치 가능

- SubModule Structure

```
lib-a/
├── pyproject.toml
├── src/
│   └── lib_a/          # 메인 패키지 (import lib_a)
│       ├── __init__.py # 여기서 'api' 모듈을 노출합니다.
│       ├── common/     # 공통 유틸리티 서브 모듈1 (패키지)
│       └── api/        # 서브 모듈2 (패키지)
│           ├── __init__.py # api 모듈의 진입점 (필수)
│           └── client.py   # api 호출 로직, 함수, 클래스 등을 작성
└── tests/
```

_`src/common`, `src/api` 형태가 아닌 `src/lib_a/common`, `src/lib_a/api` 형태 패키지 구조_

```shell
uv add lib-a
```

1. create new lib

```shell
cd src/lib
uv init lib-new --lib # lib-new 디렉토리 생성 및 기본 파일 세팅
```

2. add lib path to install_lib.sh (for docker image build)
3. add lib path to requirements-lib.txt (for ci)