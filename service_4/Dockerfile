ARG PYTHON_VERSION=3.6.8
FROM python:${PYTHON_VERSION}
WORKDIR /opt/python-flask
COPY requirements.txt /opt/python-flask
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
