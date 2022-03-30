# FROM python:3.9.2-alpine

# LABEL maintainer=a.suslov
# COPY . /app
# WORKDIR /app
# RUN pip install flask
# RUN pip install num2words

# # CMD flask run --host=0.0.0.0 -port=9991
FROM ubuntu:latest

ENV FLASK_APP testservice.py

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt

EXPOSE 9991

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]

# CMD ["python", "testservice.py"]