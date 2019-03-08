FROM tiangolo/python-machine-learning:python3.6

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN conda install tensorflow

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

CMD [ "/start.sh" ]
