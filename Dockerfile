# Dockerfile for MultLdr
FROM python:3.9

# Copy the challenge files
COPY /webapp /webapp

# Set the working directory
WORKDIR /webapp

# Set environment variable for print buffering
ENV PYTHONUNBUFFERED=1

# Install the challenge requirements
RUN pip3 install -r requirements.txt

# Install mingw toolchain
RUN apt-get update && apt-get install -y mingw-w64

# Install osslsigncode 
RUN apt-get install -y osslsigncode

# Install openssl
RUN apt-get install -y openssl

# Expose the port 5000
EXPOSE 5000

# Run the command to start the server
CMD ["python3", "run.py"]