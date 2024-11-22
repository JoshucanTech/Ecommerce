FROM python:3.13

WORKDIR /app

COPY requirements.txt

RUN pip install -r requirements

COPY . .

EXPOSE 8000

CMD ['python', 'manage.py' , 'runserver']