FROM python
COPY ./templates/index.html /home/templates/
COPY ./app.py /home/
RUN pip install flask
EXPOSE 6500
CMD [ "python3","/home/app.py" ]
