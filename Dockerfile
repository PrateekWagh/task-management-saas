FROM python:3.12
WORKDIR /main
COPY . /main
RUN pip install -r requirements
LABEL authors="myhac"

ENTRYPOINT ["top", "-b"]