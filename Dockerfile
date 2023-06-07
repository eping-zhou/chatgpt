FROM ubuntu:bionic

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install curl -y
RUN apt-get install -y gnupg2
RUN apt-get install -y p7zip-full
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
 
#Ubuntu 18.04
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt update
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install msodbcsql17 -y


# optional: for bcp and sqlcmd
RUN ACCEPT_EULA=Y apt-get install mssql-tools -y
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# optional: for unixODBC development headers
RUN apt-get install unixodbc-dev -y
RUN apt install -y python3-pip
RUN apt-get install -y python-pyodbc python3-setuptools build-essential
RUN apt-get install -y gcc 

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

ADD ctds-1.8.0-cp36-cp36m-manylinux1_x86_64.whl /usr/local/ctds-1.8.0-cp36-cp36m-manylinux1_x86_64.whl
RUN pip3 install /usr/local/ctds-1.8.0-cp36-cp36m-manylinux1_x86_64.whl

RUN apt install git -y
RUN apt-get install netcat -y
RUN mkdir /home/bert/.ssh
# ADD known_hosts /home/bert/.ssh/known_hosts

RUN pip3 install xlrd
RUN pip3 install jira
