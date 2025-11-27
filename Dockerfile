FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (if needed for future)
EXPOSE 8080

# Run consumer (modify to your main script)
CMD ["python3", "sensor_consumer_with_validation.py"]
