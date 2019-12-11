FROM ubuntu
RUN apt update
RUN apt-get install -y python3-pip python3-dev
ADD basic.py /
RUN python3 /basic.py -o /basic
ENTRYPOINT [ "python3" ]
CMD [ "basic.py" ]
