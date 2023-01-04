FROM python:3.10.9-slim-buster
RUN mkdir /app && chmod 777 /app
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN pip install --upgrade pip 
RUN apt -qq update && apt -qq install -y git ffmpeg
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash","convertor.sh"]
