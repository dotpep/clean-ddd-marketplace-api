DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} up -d
