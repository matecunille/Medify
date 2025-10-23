#!/bin/bash

# Medical Consultation System Setup Script

PROJECT_ROOT=$(dirname "$(cd "$(dirname "$0")" && pwd)")

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
if [ ! -f "$PROJECT_ROOT/docker/.env" ]; then
    echo "Creating .env file..."
    cp "$PROJECT_ROOT/.setup/env.example" "$PROJECT_ROOT/docker/.env"
    echo "✅ .env file created with default values"
else
    echo "✅ .env file already exists"
fi

# Build and run the application
echo "Building and starting the application..."
cd "$PROJECT_ROOT/docker"
docker-compose up --build -d

# After running docker-compose up
echo "Checking if the containers are running..."
sleep 5 # Wait for the services to start

# Check the status of the containers
if docker-compose -f "$PROJECT_ROOT/docker/docker-compose.yml" ps | grep -q "Exit"; then
    echo "❌ Some containers did not start correctly:"
    docker-compose -f "$PROJECT_ROOT/docker/docker-compose.yml" ps
    echo "Check the logs with: docker-compose logs"
    exit 1
else
    echo "✅ All containers are running"
    docker-compose -f "$PROJECT_ROOT/docker/docker-compose.yml" ps
    echo ""
    echo "Setup complete!"
    echo ""
    echo "Application URLs:"
    echo "   - Main App: http://localhost:8000"
    echo ""
    echo "================================================"
    echo "Useful Commands:"
    echo "To view logs: docker-compose logs"
    echo "To stop: docker-compose down"
    echo "To start: docker-compose up"
    echo "================================================"
fi

