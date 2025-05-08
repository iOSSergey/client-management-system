# Description: Dockerfile for Django application

# Stage 1: Build

FROM python:3.9-alpine AS builder

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Run

FROM python:3.9-alpine
RUN apk add --no-cache libffi openssl

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

WORKDIR /app

# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Add version number as a label
LABEL version="2025.05.08"

# Expose the port that the application will run on (adjust if necessary)
EXPOSE 8000

# Use an entrypoint script for initializing tasks
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Run the application (Django example, replace with your Flask command if needed)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "client_management_system.wsgi:application"]

