# Client Management System

## Overview

This is a Django-based application for managing clients and trips. The project is designed to help with tracking and managing client information and their associated trips.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/iOSSergey/client-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd client-management-system
   ```
3. Create a .env file in the project root directory and add the following environment variables:
   ```bash
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_NAME=your-database-name
   DATABASE_USER=your-database-user
   DATABASE_PASSWORD=your-database-password
   DATABASE_HOST=127.0.0.1
   DATABASE_PORT=3306
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/ in your web browser to view the application.

## Running with Docker

To run the application using Docker, use the following command:
```bash
docker run -d -p 8000:8000 --name cms --env-file .env client_management_system:latest
```
This will run the application in a detached mode, exposing it on port 8000, and load environment variables from the `.env` file.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues. Please ensure your changes align with the project’s coding standards and include appropriate tests.

## Contact

For any questions or inquiries, please visit https://pavlyuk.online

