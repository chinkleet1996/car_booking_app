# Use the latest Python slim image as a base
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade Python (optional)
RUN apt-get update && apt-get install -y --no-install-recommends python3.9 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Upgrade Werkzeug (optional)
RUN pip install --no-cache-dir --upgrade Werkzeug

# Copy all files
COPY . .

# Add the app directory to the Python path
ENV PYTHONPATH=/usr/src/app

# Expose port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
