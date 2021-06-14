FROM python:3.6.7-alpine

WORKDIR /app

ADD . /app

RUN pip install -U pip
RUN pip install -U setuptools
RUN python3 -m pip install --upgrade tensorflow
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]