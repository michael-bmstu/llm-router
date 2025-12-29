FROM python:3.12

WORKDIR /router

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

COPY requirements.txt router/requirements.txt

RUN pip install --no-cache-dir -r router/requirements.txt

COPY . /router

ENTRYPOINT ["python3", "main.py"]