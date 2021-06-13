FROM python:3.6.1-alpine

WORKDIR /helloWorldFlask

ADD . /helloWorldFlask

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]