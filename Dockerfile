FROM python:latest@sha256:091f21ccc2f4d319f220582c4e33801e99029f788d5767f74c8cff5396cf4fa5

RUN apt-get update && apt-get install -y \
    mdbtools \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --uid 1000  --shell /bin/bash appuser

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown -R appuser:appuser /app

USER appuser
EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]