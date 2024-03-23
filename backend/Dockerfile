# Use Python image as a base
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade Flask and Werkzeug versions
RUN pip install --no-cache-dir --upgrade Flask==2.1.0 Werkzeug==2.0.2

# Copy all files
COPY . .

# Expose port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
