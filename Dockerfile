# Build test runner image based on Python 3.12
FROM python:3.12

# Set working directory for the project
WORKDIR /app

# Copy requirements file for dependency installation
COPY requirements.txt .

# Install Python dependencies
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy project files to container
COPY . .

# Run tests with allure reporting by default
CMD ["pytest", "--alluredir", "allure-results"]