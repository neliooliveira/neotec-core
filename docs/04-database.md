# Database Schema

## Overview

PostgreSQL 15+ with Django ORM models.

## Core Tables

### Auth & Users
- auth_user (Django)
- users_role
- users_permission
- users_userrole (M2M)
- users_rolepermission (M2M)

### Multi-Tenancy
- companies_company
- companies_team
- companies_team_members (M2M)

### Clients & Projects
- clients_client
- projects_project
- projects_projectphase

### Requirements
- requirements_requirement
- requirements_requirementversion
- requirements_requirementcost
- requirements_requirementattachment
- requirements_requirementcomment

### Other Modules
- engineering_*, products_*, production_*, billing_*, documents_*, etc.

### Audit
- audit_auditlog
  - user_id, action, resource_type, resource_id
  - old_values, new_values, timestamp

---

**Document Version**: 1.0 | **Status**: In Progress 🚧