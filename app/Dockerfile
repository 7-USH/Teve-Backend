FROM python:3.9

WORKDIR /teve

ADD requirements.txt requirements.txt

ADD main.py main.py

RUN pip install -r requirements.txt

ADD teve teve

EXPOSE 8080

CMD ["python","main.py"]


