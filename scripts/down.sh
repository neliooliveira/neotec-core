#!/bin/bash
echo "🛑 Stopping NEOTEC Core services..."
docker-compose down -v
echo "✅ Services stopped and volumes removed."
