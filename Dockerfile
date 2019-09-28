FROM alpine:3.7
RUN apk add --no-cache python3 py3-pip
RUN pip3 install requests
COPY traefik.py .
ENTRYPOINT ["python3", "traefik.py"]
