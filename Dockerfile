FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --upgrade --no-cache-dir pip setuptools wheel

COPY ./src ./src
COPY ./tests ./tests

CMD ["uvicorn", "src.__main__:app", "--host", "0.0.0.0", "--port", "8000"]
