FROM python:3.8.10

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt -y install make gcc g++ default-jdk git
RUN pip3 install z3-solver==4.12.4 importlib-resources
RUN git clone https://github.com/prismmodelchecker/prism.git
RUN cd prism/prism && make && make test
RUN cp /prism/prism/bin/prism /bin/
RUN git clone https://github.com/alyziakonsta/Optimal-Observability-Problem.git
RUN cp -a /Optimal-Observability-Problem/. /


