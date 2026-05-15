# Estágio de Build
FROM python:3.10-slim as builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.10-slim

RUN useradd -m -s /bin/bash appuser
USER appuser

WORKDIR /app

COPY --from=builder /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

COPY --chown=appuser:appuser ./src ./src

EXPOSE 8000

CMD ["uvicorn", "src.__main__:app", "--host", "0.0.0.0", "--port", "8000"]
