# 🚀 NEOTEC Core - Local Setup Guide

## Quick Start (2 minutes)

### Option 1: Automated Setup (Recommended)

```bash
# Clone and enter directory
git clone https://github.com/neliooliveira/neotec-core.git
cd neotec-core

# Run setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# Wait for containers to start...
```

### Option 2: Manual Setup

```bash
# Clone
git clone https://github.com/neliooliveira/neotec-core.git
cd neotec-core

# Run quick setup
chmod +x scripts/quick-setup.sh
./scripts/quick-setup.sh
```

---

## ✅ Verify Setup

Once running, test access points:

```bash
# Frontend
curl http://localhost:3000

# Backend
curl http://localhost:8000/api

# Caddy reverse proxy
curl http://localhost

# Docker status
docker-compose ps
```

---

## 🔍 Troubleshooting

### "Cannot connect to Docker daemon"
```bash
# Start Docker service
sudo systemctl start docker          # Linux
brew services start docker            # Mac (if using Homebrew)
# Or open Docker Desktop app
```

### "Port already in use"
```bash
# Find and kill process on port
lsof -ti:3000 | xargs kill -9       # Port 3000 (Frontend)
lsof -ti:8000 | xargs kill -9       # Port 8000 (Backend)
lsof -ti:5432 | xargs kill -9       # Port 5432 (DB)
```

### "Services not responding"
```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend

# Restart all
docker-compose restart

# Or rebuild
docker-compose down -v
docker-compose up -d --build
```

### "Database connection failed"
```bash
# Wait a bit longer and try again
sleep 15
docker-compose exec backend python manage.py migrate

# Or reset database
docker-compose down -v
docker-compose up -d
```

---

## 📝 Useful Commands

```bash
# View real-time logs
docker-compose logs -f
chmod +x scripts/logs.sh
./scripts/logs.sh

# Execute Django commands
docker-compose exec backend python manage.py shell
docker-compose exec backend python manage.py createsuperuser

# Run tests
docker-compose exec backend python manage.py test

# Access database
docker-compose exec postgres psql -U neotec -d neotec_core

# Stop all services
docker-compose down

# Clean everything
docker-compose down -v
```

---

## 🌐 Remote Access (Synology NAS)

For Synology deployment:

1. SSH into Synology
2. Clone repo: `git clone https://github.com/neliooliveira/neotec-core.git`
3. Run setup: `cd neotec-core && bash scripts/setup.sh`
4. Access via: `https://your-domain.synology.me`

---

**Need help?** Check `DEVELOPMENT.md` for detailed documentation.
