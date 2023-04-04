# base image
FROM python:3.9.4
RUN pip3 install django
RUN pip3 install pillow
# set working directory
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000

# start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
