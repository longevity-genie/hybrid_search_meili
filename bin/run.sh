#!/bin/bash

# Change to the directory containing this script
cd "$(dirname "$0")"

# Move up one directory to the project root
cd ..

# Run docker-compose in the services folder
docker compose -f services/docker-compose.yaml up -d

echo "Meilisearch service started"