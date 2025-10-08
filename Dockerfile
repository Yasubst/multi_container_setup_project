# Base image
FROM python:3.10-slim

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy files from host to container
COPY ./app /app

# Installing packages
RUN pip install --no-cache-dir fastapi pydantic SQLAlchemy pymongo uvicorn

# Expose port for FastAPI
EXPOSE 8000

# Start FastAPI when container runs
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port", "8000"]
