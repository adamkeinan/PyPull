FROM python:3.9-alpine
MAINTAINER Jude Tan "adamkeinan1@gmail.com"

#
WORKDIR /djangormpi

# enviorment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# unstall system dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /src
COPY requirements.txt /djangormpi/requirements.txt
WORKDIR /src
RUN pip install --upgade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["djangoapi/apps.py"]


# copy project
COPY . .
