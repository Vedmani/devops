FROM python:3.9-slim-buster
RUN apt update -y
RUN apt install python3-pip -y
RUN pip install mysql-connector-python
RUN mkdir /app1
COPY app.py /app1/
CMD [ "python3" , "/app1/app.py" ]
