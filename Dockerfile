# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /StreamlitAzuie

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV STREAMLIT_ENV=production
ENV ANOTHER_VARIABLE=value

# Run startup.sh when the container launches
CMD ["sh", "startup.sh"]
