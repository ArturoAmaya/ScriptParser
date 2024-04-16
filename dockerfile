FROM python:bookworm

WORKDIR /code
COPY ./requirements.txt ./*.ipynb ./*.md ./*.py /code/
SHELL ["/bin/bash", "-c"]

# get ffmpeg
RUN apt-get -y update
RUN apt-get -y install ffmpeg
#RUN apt-get -y install ffprobe not necessary because ffmpeg downloaded probe as well

# set up python env
RUN python -m venv venv
RUN source ./venv/bin/activate
RUN pip install -r requirements.txt
RUN pip freeze >> reqs.txt
