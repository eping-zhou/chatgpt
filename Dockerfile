# Base image with Python
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all Python files to the working directory
COPY *.py ./

# Install required Python libraries
RUN pip install --upgrade pip
RUN pip install boto3   # AWS SDK for Python
RUN pip install pandas 
RUN pip install requests  # Library for making HTTP requests
RUN pip install beautifulsoup4  # Library for web scraping
RUN pip install psycopg2  # PostgreSQL adapter for Python

# Set the entry point to receive the filename as an argument
ENTRYPOINT ["python"]

# Default command to run if no argument is provided
CMD ["main.py"]
