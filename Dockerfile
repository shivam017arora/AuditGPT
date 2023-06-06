# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application files to the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Start the Flask application
CMD ["python", "app.py"]
