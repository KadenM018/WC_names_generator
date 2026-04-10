# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional, expand if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only dependency files first (for better caching)
COPY pyproject.toml ./

# Install dependencies
RUN pip install --upgrade pip \
    && pip install .

# Copy the rest of the application
COPY . .

# Expose port
EXPOSE 8000

# Default command (adjust module path as needed)
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]