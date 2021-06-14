FROM python:3.6.7

WORKDIR /app

ADD . /app

RUN pip install -U pip

RUN pip install tensorflow==2.5.0
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]