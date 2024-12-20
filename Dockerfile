FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose the port that the application will run on (adjust if necessary)
EXPOSE 8000

# Run the application (Django example, replace with your Flask command if needed)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "client_management_system.wsgi:application"]

