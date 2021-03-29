FROM python:3.9.1-alpine3.13
LABEL maintainer="psterne@minerva.kgi.edu"

COPY requirements.txt .

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
