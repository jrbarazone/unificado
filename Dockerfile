# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the JSON keyfile to the working directory
COPY sqlbarazone-2fdbb67f3964.json /app/sqlbarazone-2fdbb67f3964.json

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
