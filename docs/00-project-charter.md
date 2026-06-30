# Project Charter

**NEOTEC Core** - Enterprise Management Platform

## Vision Statement

NEOTEC Core é uma plataforma empresarial self-hosted que centraliza a gestão completa de clientes, projetos, engenharia, produtos, produção, costing e faturação. Alojada num Synology NAS em Docker, oferece segurança, escalabilidade e controlo total dos dados da organização.

## Business Objectives

1. **Centralizar a gestão** de todos os aspetos do negócio NEOTEC
2. **Rastrear custos** e margens com precisão desde o requisito até à faturação
3. **Melhorar a rastreabilidade** com auditoria completa
4. **Facilitar a colaboração** entre equipas internas e com clientes
5. **Otimizar a produção** com sistemas de encomenda e entrega
6. **Escalar operações** mantendo consistência e segurança

## Scope

### In Scope ✅

- Gestão de clientes e empresas
- Ciclo de vida completo de projetos
- Requisitos com versioning e custos associados
- Engenharia (hardware, firmware, software, PCB, mecânica, etc.)
- Gestão de produtos e versões
- Produção (encomendas, quantidades, entregas)
- Costing detalhado e faturação
- Documentação técnica com metadados
- Auditoria e logs de todas as operações
- Segurança com RBAC e permissões granulares
- Interface em Português e Inglês

### Out of Scope ❌

- Machine Learning / IA / LLMs / RAG / Embeddings (pgvector)
- Microserviços (arquitetura monolith modular)
- Máquinas virtuais separadas (Docker apenas)
- ChatBots ou conversational AI

## Key Stakeholders

- **Desenvolvedor**: Nelio Oliveira
- **AI Assistant**: Copilot CLI
- **Deployment Target**: Synology NAS DSM
- **Users**: NEOTEC team members

## Success Criteria

- [ ] Plataforma funcional com todos os módulos base operacionais
- [ ] Interface responsiva e intuitiva
- [ ] Todos os dados auditados e rastreáveis
- [ ] Custos de projetos corretamente associados
- [ ] Deploy bem-sucedido em Synology NAS
- [ ] Documentação completa para manutenção e operação
- [ ] Testes cobrindo funcionalidades críticas

## Timeline (Indicativo)

| Fase | Duração | Metas |
|------|---------|-------|
| **0. Setup** | 1 semana | Estrutura, Docker, models base |
| **1. Core** | 3 semanas | Autenticação, users, companies, clients |
| **2. Projects & Reqs** | 3 semanas | Projects, requirements com versioning |
| **3. Costing & Billing** | 2 semanas | Custos e faturação |
| **4. Production** | 2 semanas | Encomendas e produção |
| **5. Polish & Deploy** | 2 semanas | UI/UX refinement, documentação, deploy |

## Technology Stack

### Backend
- Python 3.12+
- Django 5.x / Django REST Framework
- PostgreSQL 15+
- Celery (async tasks)

### Frontend
- Next.js 14+ (TypeScript)
- React 18+
- TailwindCSS
- i18n (pt-PT & en)

### Infrastructure
- Docker Compose
- Caddy (reverse proxy, HTTPS, WAF)
- Valkey (caching, sessions)
- PostgreSQL (primary database)

## Deployment

**Target**: Synology NAS (DSM)
- Container Manager (Docker support)
- Network isolation
- HTTPS via Caddy
- Automated backups

## Constraints & Assumptions

**Constraints**
- Deve rodar em Docker no Synology
- Sem VMs ou containers separados (além do compose)
- Interface obrigatoriamente em pt-PT e en
- Dark mode como default
- Sem IA/LLMs/RAG

**Assumptions**
- PostgreSQL disponível ou provisionado
- HTTPS obrigatório em produção
- Dados sensíveis devem estar isolados por company/tenant
- Backend e frontend em containers separados

## Approval & Sign-off

| Papel | Nome | Data | Assinatura |
|-------|------|------|-----------|
| Product Owner | NEOTEC | 2026-06-30 | ✓ |
| Tech Lead | neliooliveira | 2026-06-30 | ✓ |
| AI Assistant | Copilot | 2026-06-30 | ✓ |

---

**Document Version**: 1.0  
**Last Updated**: 2026-06-30  
**Status**: Active ✅
