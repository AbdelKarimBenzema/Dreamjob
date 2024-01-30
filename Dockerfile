FROM python:3.8.18
RUN mkdir /app
WORKDIR /app
ADD ./web .
RUN pip install -r requirements.txt

EXPOSE 8080

# Run app.py when the container launches
#CMD ["python", "./app.py"]
CMD ["python", "app.py", "runserver"]