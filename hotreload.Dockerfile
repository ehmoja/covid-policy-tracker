FROM python:3.7-slim

VOLUME [ "/app/static" ]

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app
RUN python3 setup.py install

ENV PROJECT_ROOT=/app
ENTRYPOINT [ "python3" ]
CMD [ "app/wsgi.py" ]
