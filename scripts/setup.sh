#!/bin/bash

# Medical Consultation System Setup Script

echo "Setting up Medify - Medical Consultation System"
echo "================================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f "src/.env" ]; then
    echo "Creating .env file..."
    cat > src/.env << EOL
DEBUG=True
SECRET_KEY=django-insecure-change-this-in-production
DB_NAME=medify_db
DB_USER=medify_user
DB_PASSWORD=medify_password_123
DB_HOST=db
DB_PORT=3306
DB_ROOT_PASSWORD=root_password_123
EOL
    echo "✅ .env file created with default values"
else
    echo "✅ .env file already exists"
fi

# Build and run the application
echo "Building and starting the application..."
cd docker
docker-compose up --build -d

echo ""
echo "Setup complete!"
echo ""
echo "Application URLs:"
echo "   - Main App: http://localhost:8000"
echo "   - Admin Panel: http://localhost:8000/admin"
echo ""
echo "To view logs: docker-compose logs -f"
echo "To stop: docker-compose down"