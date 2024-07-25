# Use the ultralytics/ultralytics:latest as the base image
FROM ultralytics/ultralytics:latest-arm64

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]