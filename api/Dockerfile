# # api/Dockerfile
# FROM arm64v8/python:3.10.5

# WORKDIR /app

# # COPY requirements.txt .

# # RUN python -m venv .venv
# # RUN /bin/bash -c "source .venv/bin/activate"
# # RUN /bin/sh -c pip install --no-cache-dir -r requirements.txt
# # RUN /bin/sh -c uvicorn main:app --host 0.0.0.0 --port 8000

# RUN pip install --upgrade pip
# CMD ["/bin/bash", "-c", "python -m venv .venv && source .venv/bin/activate && pip install --no-cache-dir -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 8000"]


# COPY . .

FROM arm64v8/python:3.10.5

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
