#!/bin/bash
set -e

# Wait for database to be ready
echo "Waiting for database to be ready..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Database is ready!"

# Check for proper Alembic initialization
if [ ! -f "migrations/env.py" ]; then
    echo "Initializing migrations..."
    rm -rf migrations  # In case it's a broken or partial folder
    flask db init
fi

# Create and apply migrations
echo "Creating migrations..."
flask db migrate -m "Initial migration" || echo "Migration already exists or nothing to migrate."

echo "Applying migrations..."
flask db upgrade

# Start the Flask application
echo "Starting Flask application..."
exec flask run --host=0.0.0.0 --port=5008
