FROM python:3.9.2-alpine

ENV FLASK_APP testservice.py

COPY . /app
WORKDIR /app 

RUN pip install flask
RUN pip install num2words

EXPOSE 3000

ENTRYPOINT ["python", "-m", "flask", "run", "--port=3000", "--host=0.0.0.0"]