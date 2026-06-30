# Functional Specification

## Overview

This document defines the functional requirements and features of NEOTEC Core.

## Core Modules

### 1. Users Module (`apps/users`)

**Purpose**: Authentication, authorization, and user management.

**Models**:
- User
  - username, email, full_name, avatar
  - is_active, is_staff, is_superuser
  - company_id (FK to Company)
  - created_at, updated_at

- Role
  - name (Admin, Manager, Engineer, Finance, Client, Support)
  - description
  - company_id (FK)

- Permission
  - codename (create_project, edit_requirement, etc.)
  - name, description
  - created_at

**API Endpoints**:
- POST /api/auth/login - User login
- POST /api/auth/logout - User logout
- GET /api/users/{id} - Get user details
- PATCH /api/users/{id} - Update user

### 2. Companies Module (`apps/companies`)

**Purpose**: Organization management and multi-tenancy.

**Key Features**:
- Company profiles
- Team management
- Multi-tenancy support
- Audit logging

### 3. Clients Module (`apps/clients`)

**Purpose**: Client/customer management.

**Key Features**:
- Client profiles
- Contact information
- Status tracking
- Relationship to projects

### 4. Projects Module (`apps/projects`)

**Purpose**: Project management and lifecycle.

**Key Features**:
- Project lifecycle (planning → active → completed)
- Budget tracking
- Phase management
- Margin calculation

### 5. Requirements Module (`apps/requirements`)

**Purpose**: Living requirements management with versioning and costing.

**Key Features**:
- Requirements with full version history
- Cost tracking (estimated vs approved)
- Attachments (images, videos, documents)
- Comments and discussion
- Status and priority management
- Complete audit trail

### 6-13. Other Core Modules

**Engineering, Products, Production, Billing, Documents, Notifications, Audit** - Detailed in subsequent phases.

---

**Document Version**: 1.0 | **Status**: In Progress 🚧