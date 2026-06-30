# Development Instructions

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.12+ (for local development)
- Node.js 18+ (for frontend development)
- PostgreSQL 15+ (if running locally without Docker)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/neliooliveira/neotec-core.git
cd neotec-core

# 2. Run setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# 3. Access the platform
# Frontend:    http://localhost:3000
# Backend API: http://localhost:8000/api
# Admin:       http://localhost:8000/admin
```

## Development Workflow

### Backend Development

```bash
# Create new model
cd backend
python manage.py startapp my_app apps/my_app

# Make migrations
./scripts/makemigrations.sh
# or: docker-compose exec backend python manage.py makemigrations

# Run migrations
./scripts/migrate.sh

# Run tests
./scripts/test.sh

# Run linters
./scripts/lint.sh
```

### Frontend Development

```bash
# Install dependencies
cd frontend
npm install

# Start dev server
npm run dev

# Type check
npm run type-check

# Build for production
npm run build
```

### Docker Commands

```bash
# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Access Django shell
docker-compose exec backend python manage.py shell

# Access database
docker-compose exec postgres psql -U neotec -d neotec_core

# Rebuild containers
docker-compose build

# Stop and remove all
./scripts/clean.sh
```

## Database

### Accessing PostgreSQL

```bash
# From Docker
docker-compose exec postgres psql -U neotec -d neotec_core

# Credentials (from .env)
User: neotec
Password: (see .env)
Database: neotec_core
Host: localhost
Port: 5432
```

### Common Queries

```sql
-- List all tables
\dt

-- Export database
pg_dump -U neotec -d neotec_core > backup.sql

-- Import database
psql -U neotec -d neotec_core < backup.sql
```

## Deployment

### Synology NAS

See `docs/deployment-synology.md` for detailed instructions.

### Local Production

```bash
# Build images
docker-compose -f docker-compose.yml build

# Run in production mode
DJANGO_ENVIRONMENT=production docker-compose up -d
```

## Testing

### Backend Tests

```bash
# Run all tests
docker-compose exec backend python manage.py test

# Run specific app tests
docker-compose exec backend python manage.py test apps.users

# Run with coverage
docker-compose exec backend coverage run --source='.' manage.py test
docker-compose exec backend coverage report
```

### Frontend Tests (TODO)

```bash
npm test
```

## Code Style

### Backend (Python)

- **Formatter**: Black
- **Linter**: Flake8
- **Type checking**: mypy (when added)

```bash
pip install black flake8
black .
flake8 .
```

### Frontend (TypeScript)

- **Formatter**: Prettier
- **Linter**: ESLint

```bash
npm install prettier eslint
npx prettier --write .
npm run lint
```

## Troubleshooting

### Port Already in Use

```bash
# Kill process on port
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:3000 | xargs kill -9  # Frontend
lsof -ti:5432 | xargs kill -9  # Database
```

### Database Connection Issues

```bash
# Check PostgreSQL is running
docker-compose ps | grep postgres

# Rebuild database
./scripts/clean.sh
./scripts/setup.sh
```

### Django Migration Conflicts

```bash
# Revert migrations
./scripts/revert-migrations.sh users

# Start fresh
python manage.py migrate users zero
```

## Contributing

1. Create feature branch: `git checkout -b feature/description`
2. Make changes and test
3. Commit: `git commit -m "feat: description"`
4. Push: `git push origin feature/description`
5. Create Pull Request

## Documentation

Keep documentation updated:
- Code changes → Update docstrings
- API changes → Update API documentation
- Database changes → Update database schema
- New features → Add to feature list

---

**Last Updated**: 2026-06-30
