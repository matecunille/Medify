# Sistema de Gestión de Consultas Médicas

Este proyecto es una aplicación web desarrollada en Django para la gestión de consultas médicas entre pacientes y médicos.

## Requisitos

- asgiref==3.9.0
- Django==5.2.4
- django-widget-tweaks==1.5.0
- mysqlclient==2.2.7
- pillow==11.3.0
- python-dotenv==1.1.1
- sqlparse==0.5.3
- tzdata==2025.2

## Configuración Inicial

1. **Crear la base de datos**

   Crear la base de datos manualmente, debido a que django no la crea automaticamente, usar DataGrip, MySQLWorkBench o bien atraves del shell de MySQL.

2. **Configurar variables de entorno**

   Modificar el archivo `.env` en la raíz del proyecto(dentro de Programacion_3) con el siguiente contenido:

   ```env
   DATABASE_NAME=nombre_base
   DATABASE_USER=usuario
   DATABASE_PASSWORD=password
   DEBUG=TRUE
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones a la base de datos**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Iniciar la aplicacion**

   ```bash
   python manage.py runserver
   ```

## Como usar

- Accede a la aplicación en [http://localhost:8000](http://localhost:8000)
- Crear superUser y acceder al admin, posteriormente crear especialidades asi se puede crear un medico
- Regístrate como paciente o médico para comenzar a gestionar consultas.

---
