FROM python:3.13
WORKDIR /usr/local/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
    
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*    

# Install Dependencies    
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src .

# Copy entrypoint script before switching users
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Its good practice to setup a user, so that the container doesnt run on root
RUN useradd -m app && chown -R app:app /usr/local/app
USER app

EXPOSE 8080

ENTRYPOINT ["sh", "/usr/local/bin/entrypoint.sh"]