FROM python:3.9.2-alpine

ENV FLASK_APP testservice.py

COPY . /app
WORKDIR /app 

RUN pip install flask
RUN pip install num2words

EXPOSE 9991

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=9991"]