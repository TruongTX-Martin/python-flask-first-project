FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /var/www
WORKDIR /var/www

COPY requirements.txt /var/www
RUN pip install -r requirements.txt

COPY . /var/www/app
WORKDIR /var/www/app
CMD ["python", "manage.py", "run"]
