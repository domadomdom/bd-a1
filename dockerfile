FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /home/doc-bd-a11/

COPY iris.data .

RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

CMD ["bash"]

