#!/bin/bash
echo "🐳 NEOTEC Core - Viewing logs"
echo "=============================="
echo ""
echo "Choose service to view:"
echo "1) Backend (Django)"
echo "2) Frontend (Next.js)"
echo "3) Database (PostgreSQL)"
echo "4) Cache (Valkey)"
echo "5) Caddy (Reverse Proxy)"
echo "6) All services"
echo ""
read -p "Enter choice (1-6): " choice

case $choice in
    1) docker-compose logs -f backend ;;
    2) docker-compose logs -f frontend ;;
    3) docker-compose logs -f postgres ;;
    4) docker-compose logs -f valkey ;;
    5) docker-compose logs -f caddy ;;
    6) docker-compose logs -f ;;
    *) echo "Invalid choice" ;;
esac
