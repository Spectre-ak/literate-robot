FROM python:3.6.1-alpine

WORKDIR /app

ADD . /app

RUN pip install -U pip
RUN pip install -U setuptools
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]