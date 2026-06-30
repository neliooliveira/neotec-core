# NEOTEC Core Backend - README

## Local Development

### Prerequisites
- Python 3.12+
- PostgreSQL 15+
- Valkey or Redis

### Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load initial data (optional)
python manage.py seed_initial_data

# Run development server
python manage.py runserver 0.0.0.0:8000
```

### Docker

```bash
# From project root
cd ..
docker-compose up -d
```

### Structure

```
backend/
├── core/                    # Django project settings
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── testing.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/                    # Django apps
│   ├── users/
│   ├── companies/
│   ├── clients/
│   ├── projects/
│   ├── requirements/
│   ├── engineering/
│   ├── products/
│   ├── production/
│   ├── billing/
│   ├── documents/
│   ├── notifications/
│   ├── audit/
│   └── knowledge_base/
│
├── middleware/              # Custom middleware
├── permissions/             # Permission classes
├── utils/                   # Utilities
├── tests/                   # Test utilities
├── manage.py
└── requirements.txt
```

---

**Status**: 🚧 In Development
