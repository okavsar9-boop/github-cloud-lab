# Using Alpine for a more compact footprint
FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set non-root user for security (Bonus different approach)
USER 1000

CMD ["pytest", "tests/", "-v"]
