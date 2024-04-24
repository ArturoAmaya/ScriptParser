# THIS IS THE JUPYTER DOCKERFILE
FROM python:3.12

RUN curl -o ffmpeg.tar.xz https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz
RUN tar -xf ffmpeg.tar.xz && mv ffmpeg-git-20240301-amd64-static ffmpeg
#RUN apt-get -y install ffprobe not necessary because ffmpeg downloaded probe as well
ENV PATH="${PATH}:/code/ffmpeg"
# install the notebook package
RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache notebook jupyterlab


# create user with a home directory
ARG NB_USER=joyvan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN curl -o ffmpeg.tar.xz https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz
RUN tar -xf ffmpeg.tar.xz && mv ffmpeg-git-20240301-amd64-static ffmpeg
#RUN apt-get -y install ffprobe not necessary because ffmpeg downloaded probe as well


RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}
USER ${USER}

COPY . ${HOME}
ENV PATH="${PATH}:/ffmpeg"
#docker build -t jupyter .
#docker run -it --rm -p 8888:8888 jupyter jupyter notebook --NotebookApp.default_url=/lab/ --ip=0.0.0.0 --port=8888