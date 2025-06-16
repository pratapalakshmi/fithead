#!/bin/bash
set -e

# Wait for database to be ready
echo "Waiting for database to be ready..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Database is ready!"

# Initialize migrations if they don't exist
if [ ! -d "migrations" ]; then
    echo "Initializing migrations..."
    flask db init
fi

# Create and apply migrations
echo "Creating migrations..."
flask db migrate -m "Initial migration"

echo "Applying migrations..."
flask db upgrade

# Start the Flask application
echo "Starting Flask application..."
exec flask run --host=0.0.0.0 --port=5000