FROM python:3.12.1-slim

WORKDIR /app/

RUN apt-get update && apt-get upgrade -y
RUN python -m pip install --upgrade pip

COPY ./ /app
RUN cd /app

RUN pip install -r requirements.txt

RUN chmod +x start.sh

ENV PATH=$PATH:/app

EXPOSE 8080
RUN export PORT=8080

CMD ["start.sh"]