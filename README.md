# 🏥 Medify - Medical Consultation System

A modern Django-based web application for managing medical consultations between doctors and patients.

## Features

- **User Management**: Separate roles for patients and doctors
- **Consultation Scheduling**: Easy appointment booking system
- **Specialty Management**: Organize doctors by medical specialties
- **Responsive Design**: Modern Bootstrap-based UI
- **Docker Ready**: Containerized deployment
- **Admin Interface**: Built-in Django admin for system management

## Technology Stack

- **Backend**: Django 5.2.4
- **Database**: MySQL 8.0
- **Frontend**: Django templates and Bootstrap 5.3
- **Containerization**: Docker & Docker Compose
- **Static Files**: WhiteNoise for efficient serving
- **Authentication**: Django built-in authentication system

## Project Structure

```
medical-consultation-system/
├── README.md
├── requirements.txt
├── .gitignore
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── entrypoint.sh
│   └─ .env
├── docs/
└── src/
    ├── manage.py
    ├── config/          # Django settings
    ├── users/           # User management app
    ├── consultations/   # Consultation management app
    ├── templates/       # HTML templates
    └── static/          # CSS, JS, images
```

## Development Setup

### Prerequisites

- Docker & Docker Compose
- Git

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/matecunille/Programacion_3.git
   cd Programacion_3
   ```

2. **Environment Setup**

   ```bash
   cd setup
   ./setup.sh
   ```

3. **Run with Docker**

   ```bash
   cd docker
   docker-compose up --build
   ```

4. **Access the application**
   - Application: <http://localhost:8000>
   - Admin Panel: <http://localhost:8000/admin>

## 🏃‍♂️ Usage

### For Patients

- Register with patient role
- Browse available doctors by specialty
- Schedule consultations
- View consultation history

### For Doctors

- Register with doctor role and specialty
- View assigned consultations
- Update consultation status
- Manage patient appointments

### For Administrators

- Access Django admin panel
- Manage users, specialties, and consultations
- System configuration and monitoring