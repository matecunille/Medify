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
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG APP_UID=1000
ARG APP_GID=1000
RUN groupadd -g $APP_GID app \
 && useradd -m -u $APP_UID -g $APP_GID app

COPY --chown=app:app src/ .
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

RUN mkdir -p /usr/local/app/staticfiles /usr/local/app/media \
 && chown -R app:app /usr/local/app/staticfiles /usr/local/app/media \
 && chmod -R 755 /usr/local/app/staticfiles /usr/local/app/media

USER app
EXPOSE 8000
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
