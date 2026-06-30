#!/bin/bash
echo "🧹 Cleaning up NEOTEC Core containers and volumes..."
docker-compose down -v
docker system prune -f
echo "✅ Cleanup complete."
