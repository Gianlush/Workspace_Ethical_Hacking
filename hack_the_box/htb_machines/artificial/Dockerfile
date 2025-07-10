FROM python:3.8

# Install necessary tools and libraries
RUN pip install --no-cache-dir tensorflow pandas

# Create working directory
WORKDIR /app

# Entrypoint to dynamically execute a script passed from outside
ENTRYPOINT ["python"]


# to run scripts in python3.8
# docker run --rm -v "$PWD":/app artificial exploit.py
