# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8080

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV AWS_ACCESS_KEY_ID=AKIAQUVKBKU7WULLIWIT
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_STORAGE_BUCKET_NAME=neox-development-s3
ENV AWS_MEDIA_LOCATION=media

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]