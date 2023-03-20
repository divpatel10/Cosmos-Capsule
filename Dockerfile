# Base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt /app

# Install the dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

# Expose port 80
EXPOSE 80

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "80"]