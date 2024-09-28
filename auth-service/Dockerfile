# Base image with Python and Flask
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV FLASK_APP=auth_service.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port
EXPOSE 5003

# Run the application
CMD ["flask", "run"]

