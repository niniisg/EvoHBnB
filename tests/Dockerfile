
FROM python:3.8-alpine

WORKDIR /user/src/app


COPY . .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY  entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "executable" ]


ENV PORT 8000


EXPOSE 8000


VOLUME ["/app/data"]
