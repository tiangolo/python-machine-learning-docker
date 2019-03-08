FROM tiangolo/python-machine-learning:cuda9.1-python3.6

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

# cudatoolkit=9.1 is not available yet in Conda
RUN conda install tensorflow-gpu cudatoolkit=9.0

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

CMD [ "/start.sh" ]
