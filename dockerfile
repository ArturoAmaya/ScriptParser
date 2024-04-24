FROM python:bookworm
SHELL ["/bin/bash", "-c"]

WORKDIR /code
COPY . /code/
#./scriptparser/. ./requirements.txt ./*.ipynb ./*.md ./*.py /code/

# get ffmpeg
RUN apt-get -y update
RUN apt-get -y install ffmpeg
#RUN apt-get -y install ffprobe not necessary because ffmpeg downloaded probe as well

# set up python env
RUN python -m venv venv
RUN source ./venv/bin/activate
RUN pip install -r requirements.txt
#RUN pip freeze >> reqs.txt

## 
# build with docker build -t script_parser:[V#] .
# run interactive image with docker run -it --entrypoint bash script_parser:[v#]