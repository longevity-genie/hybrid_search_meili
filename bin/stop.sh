#!/bin/bash

# Change to the directory containing this script
cd "$(dirname "$0")"

# Move up one directory to the project root
cd ..

# Stop docker-compose services in the services folder
docker compose -f services/docker-compose.yaml down

echo "Meilisearch service stopped"