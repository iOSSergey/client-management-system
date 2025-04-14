#!/bin/sh

# Ensure the script stops execution on errors
set -e

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations (опционально, если нужно)
echo "Applying database migrations..."
python manage.py migrate --noinput

# Execute the main process specified in CMD
exec "$@"