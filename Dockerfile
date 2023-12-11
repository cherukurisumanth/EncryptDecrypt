ARG REGISTRY="docker.io"
ARG REPOSITORY="library"
ARG IAMGE="alpine"
ARG TAG="latest"

FROM ${REGISTRY}/${REPOSITORY}/${IAMGE}:${TAG}

LABEL maintainer="watashi"
LABEL description="encryption and decryption application"

USER root
WORKDIR /usr/src/app
COPY requirements.txt .
RUN apk --no-cache add python3
RUN apk --no-cache add py3-pip
RUN pip install --trusted-host pypi.org --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8585
ENTRYPOINT ["python3", "entrypoint.py"]