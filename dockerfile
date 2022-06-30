FROM python:3.9-slim-buster

#Update
RUN apt update -y && apt upgrade -y
RUN python3 -m pip install --upgrade pip

EXPOSE 8080

COPY ./src /home

CMD ["python3", "/home/main.py"]