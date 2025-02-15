# Use Python base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
