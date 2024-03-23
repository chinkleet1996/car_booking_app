# Use Python 3.9 slim image as a base
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Update package list and install required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.9 as the default Python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Add the app directory to the Python path
ENV PYTHONPATH=/usr/src/app

# Expose port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
