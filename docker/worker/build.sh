#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

REGISTRY="${REGISTRY:-airflow-boilerplate}"

REGISTRY="$(printf %s "$REGISTRY" | tr "[:upper:]" "[:lower:]")"
TAG="${TAG:-$(git describe --always --dirty --abbrev=7 2>/dev/null || echo dev)}"
DEPS_GROUP="${DEPS_GROUP:-common}"
PUSH="${PUSH:-0}"

base="$REGISTRY/worker-base:$TAG"
docker build -f docker/worker/base/Dockerfile \
  --build-arg DEPS_GROUP="$DEPS_GROUP" \
  -t "$base" -t "$REGISTRY/worker-base:dev" .

for worker in "${@:-default}"; do
  image="$REGISTRY/worker-$worker:$TAG"
  docker build -f "docker/worker/$worker/Dockerfile" \
    --build-arg BASE_IMAGE="$base" \
    -t "$image" -t "$REGISTRY/worker-$worker:dev" .
  if [ "$PUSH" = 1 ]; then docker push "$image"; fi
  echo "built $image (+ :dev)"
done


echo "tag=$TAG" >> "${GITHUB_OUTPUT:-/dev/null}"
