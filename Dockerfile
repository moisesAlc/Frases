FROM python:3.12 

RUN mkdir /usr/src/app

COPY app.py /usr/src/app

COPY requirements.txt frases.json /usr/src/app/

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]