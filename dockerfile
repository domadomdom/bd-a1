FROM ubuntu

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir /home/doc-bd-a1

COPY diabetes.csv /home/doc-bd-a1/

CMD ["/bin/bash"]
