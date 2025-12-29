FROM python:3.12

WORKDIR /router

COPY requirements.txt router/requirements.txt

RUN pip install --no-cache-dir r- router/requirements.txt

COPY . /router

ENTRYPOINT ["python3", "main.py"]