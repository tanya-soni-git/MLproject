# Use official Python slim image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from current directory to /app inside the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask app using gunicorn (production WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
