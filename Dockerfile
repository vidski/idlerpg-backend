FROM python:3.12-slim-bullseye

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# for pip cache:
ENV XDG_CACHE_HOME=/var/cache

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc libpq-dev zlib1g-dev libxml2-dev libxslt-dev libmagic1 git locales  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the locale
RUN sed -i '/de_DE.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG=de_DE.UTF-8
ENV LANGUAGE=de_DE:de
ENV LC_ALL=de_DE.UTF-8


# Upgrade pip
RUN pip install --upgrade pip

# Copy application files
WORKDIR /service
COPY . /service

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint script as executable
RUN chmod +x /service/docker/django/entrypoint.sh

# Clean up
RUN apt-get clean && apt-get autoclean && rm -rf /tmp/* /var/lib/apt/lists/*

EXPOSE 8000