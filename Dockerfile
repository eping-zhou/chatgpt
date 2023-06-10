FROM ubuntu:20.04

RUN apt update
RUN apt -y upgrade

RUN apt install -y curl gnupg2 p7zip-full

# optional: for unixODBC development headers
RUN apt install unixodbc-dev -y
RUN apt install -y python3-pip
RUN apt install -y python3-pyodbc python3-setuptools build-essential
RUN apt install -y gcc 

RUN useradd --create-home --shell /bin/bash bert

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN pip3 install -U pip
RUN pip3 install awscli boto3 openpyxl pyodbc requests_aws_sign pykeepass pysftp sqlparse pillow
RUN pip3 install parameterized coverage
RUN pip3 install XlsxWriter
RUN pip3 install tableauserverclient PyPDF2 jinja2
RUN pip3 install pymssql
RUN pip3 install python-jenkins
RUN pip3 install python-gitlab
RUN pip3 install pandas
RUN pip3 install msoffcrypto-tool

RUN apt install git -y
RUN apt install netcat -y
RUN mkdir /home/bert/.ssh
# ADD known_hosts /home/bert/.ssh/known_hosts

RUN pip3 install xlrd
RUN pip3 install jira
