# NEOTEC Core

Enterprise platform for client, project, and production management.

**Self-hosted on Synology NAS** | Docker | PostgreSQL | Django + DRF | Next.js | TypeScript

---

## 📋 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.12+
- Node.js 18+
- PostgreSQL 15+

### Development

```bash
# Clone the repository
git clone https://github.com/neliooliveira/neotec-core.git
cd neotec-core

# Copy environment files
cp .env.example .env

# Build and start containers
docker-compose up -d

# Access the platform
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api
- Admin: http://localhost:8000/admin
```

### Documentation

- **[Project Charter](docs/00-project-charter.md)** - Scope and objectives
- **[Vision](docs/01-vision.md)** - Detailed platform vision
- **[Functional Specification](docs/02-functional-specification.md)** - Requirements and features
- **[Architecture](docs/03-architecture.md)** - System design and components
- **[Database](docs/04-database.md)** - Schema and relationships
- **[Security](docs/05-security.md)** - Security strategy and implementation
- **[UI/UX](docs/06-ui-ux.md)** - Design principles and guidelines

## 🏗️ Architecture

### Technology Stack

**Backend**
- Python 3.12+
- Django 5.x
- Django REST Framework
- PostgreSQL 15+

**Frontend**
- Next.js 14+ (TypeScript)
- React 18+
- TailwindCSS
- i18n (pt-PT & en)

**Infrastructure**
- Docker Compose
- Caddy (reverse proxy, HTTPS)
- Valkey (caching)
- PostgreSQL (database)

### Core Modules

- **users** - Authentication, RBAC, audit logging
- **companies** - Company/organization management
- **clients** - Client information and relationships
- **projects** - Project management and lifecycle
- **requirements** - Living requirements with versioning and costing
- **engineering** - Engineering disciplines and documentation
- **products** - Product management and versions
- **production** - Orders, manufacturing, and delivery
- **billing** - Invoicing, costs, and margins
- **documents** - Technical documentation with metadata
- **notifications** - Real-time notifications
- **audit** - Complete audit trail

## 🔒 Security First

- RBAC with granular permissions
- HTTPS via Caddy
- Backend isolated from frontend
- Data isolation per company
- Internal costs hidden from clients
- Audit trail for all operations

## 🎨 UI/UX Principles

- **Dark mode first** - Optimized for dark theme
- **Fast & fluid** - Smooth interactions and transitions
- **Intuitive** - Inspired by Apple, Linear, Notion, Figma
- **Clean** - Minimalist, modern design
- **Accessible** - Portuguese (pt-PT) and English from day one

## 📦 Project Structure

```
neotec-core/
├── docs/                    # Documentation
│   ├── 00-project-charter.md
│   ├── 01-vision.md
│   ├── 02-functional-specification.md
│   ├── 03-architecture.md
│   ├── 04-database.md
│   ├── 05-security.md
│   └── 06-ui-ux.md
├── backend/                 # Django project
│   ├── core/               # Main Django settings
│   ├── apps/               # Django apps
│   ├── static/
│   ├── media/
│   ├── manage.py
│   └── requirements.txt
├── frontend/                # Next.js project
│   ├── app/                # Next.js app directory
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── styles/
│   └── package.json
├── infra/                   # Infrastructure & deployment
│   ├── docker/
│   ├── caddy/
│   └── synology/           # Synology-specific configs
├── scripts/                 # Utility scripts
└── docker-compose.yml       # Local development
```

## 🚀 Deployment

### Local Development
```bash
docker-compose up -d
```

### Synology NAS
See [Synology Deployment Guide](docs/deployment-synology.md)

## 📝 Development Guidelines

- **Branch naming**: `feature/`, `fix/`, `docs/`
- **Commits**: Clear, descriptive messages
- **Code style**: Black (Python), Prettier (TypeScript)
- **Testing**: Unit and integration tests required
- **Documentation**: Always keep docs updated

## 📄 License

Proprietary - NEOTEC

## 👤 Team

- **Initial Development**: Copilot + neliooliveira

---

**Status**: 🚧 In Development | **Version**: 0.1.0
