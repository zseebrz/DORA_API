FROM python:3.7.10-slim-buster

RUN pip install --upgrade pip

RUN apt update
RUN apt-get update
RUN apt-get -y install git

#to see what's going on
ENV PYTHONUNBUFFERED 1

#Based on Emanuele's dockerfiles for ecadockerhub
# Create a non-root user
# Please match this with host machine desired uid and gid
RUN groupadd -r --gid 1000 python # 901 for ecadockerhub, 1000 for generic ubuntu 20 installations
RUN useradd --no-log-init --uid 1000 -r -m -g python python # 954 for ecadockerhub, 1000 for generic ubuntu 20 installations
ENV PATH=$PATH:/home/python/.local/bin


# Create the work dir and set permissions as WORKDIR set the permissions as root
RUN mkdir /home/python/app/ && chown -R python:python /home/python/app
ADD . /home/python/app
WORKDIR /home/python/app

USER python

#RUN cd /home/python/app/
#RUN git clone https://github.com/zseebrz/DORA_API ./DORA_API

ENV PATH="/home/worker/.local/bin:${PATH}"

RUN pip install --user -r /home/python/app/requirements.txt

#need to install NLTK tokenizers manually:
RUN python -m nltk.downloader punkt

COPY --chown=python:python . .

#RUN cd /home/python/app/
#RUN python main.py
#or run the shell script: run.sh

CMD ["python", "main.py"]
EXPOSE 8000
