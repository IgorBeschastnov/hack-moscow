FROM python:3.7

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8001

RUN chmod +x run.sh
ENTRYPOINT [ "/app/run.sh" ]
