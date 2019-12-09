FROM python:3.7
COPY . /app
WORKDIR /app
RUN apt-get update && \
    pip install -r requirements.txt --no-cache-dir
CMD python ./main.py