FROM python:3.6.8

WORKDIR /Puyuan

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /Puyuan

RUN pip install -r requirements.txt

COPY . /Puyuan

EXPOSE 8000

CMD [ "python", "manage.py", "runserver","0.0.0.0:8000" ]