# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim as base_stage
# create project directory
RUN mkdir -p /app && chmod -R 700 /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

# change directory
WORKDIR /app

# expose app port
EXPOSE 3000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# setup flask environment
ENV FLASK_APP=src.app
ENV FLASK_ENV=development
ENV SESSION_SECRET=development_secret

# change user
USER appuser

# PRODUCTION STAGE
FROM base_stage as production_stage
# change env to production
ENV FLASK_ENV=production
ENV SESSION_SECRET=

# copy project
COPY --chown=appuser . /app

# During debugging, this entry point will be overridden.
# For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "60", "--workers", "4", "--threads", "4", "src.app:app"]
