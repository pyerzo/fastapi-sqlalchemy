FROM python:3.10
ENV PYTHONUNBUFFERED 1
COPY start /start
COPY entrypoint /entrypoint
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip debugpy -t /tmp
RUN rm -rf /tmp/requirements && rm -vrf /var/cache/apk/*
COPY ./app /code/app
WORKDIR /code
ENTRYPOINT ["/entrypoint"]