# Base image with Python and Flask
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV FLASK_APP=upload_service.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port
EXPOSE 5001

# Run the application
CMD ["flask", "run"]

