FROM ghcr.io/marimo-team/marimo:latest

WORKDIR /app

# Copy all files to the container
COPY . /app

# Install Python dependencies
RUN pip install pandas==2.3.3 numpy==2.3.5 openpyxl

# Expose port 8080
EXPOSE 8080

# Run marimo in app mode (read-only)
CMD ["marimo", "run", "explore_city_tax_data.py", "--host", "0.0.0.0", "--port", "8080"]
