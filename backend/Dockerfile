# Use Python 3.9 slim buster image as a base
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /usr/src/app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade Flask and Werkzeug to compatible versions
RUN pip install --no-cache-dir Flask==2.1.0 Werkzeug==2.0.2

# Copy all files
COPY . .

# Add the app directory to the Python path
ENV PYTHONPATH=/usr/src/app

# Expose port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
