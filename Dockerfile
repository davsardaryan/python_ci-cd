# Write Dockerfile instructions for python app expose port 5000



# Use the official Python base image
FROM python:3

# Set the working directory in the container
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the image
COPY . .

# Expose port 5000
EXPOSE 5000

# Define the command to start the application
CMD ["python", "./app.py"]

