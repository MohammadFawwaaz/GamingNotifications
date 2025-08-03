FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
COPY requirements-test.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Only install test dependencies when needed
ARG INSTALL_TESTS=false
RUN if [ "$INSTALL_TESTS" = "true" ] ; then pip install -r requirements-test.txt ; fi

COPY . .

# Set PYTHONPATH for module discovery
ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]