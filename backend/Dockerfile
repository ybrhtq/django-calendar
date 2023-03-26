FROM python:3.11.2

WORKDIR /backend

COPY ./requirements/debian ./requirements/debian
RUN apt-get update; apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y \
    && grep -o "^[^#]*" requirements/debian/requirements.txt | xargs apt-get install -y

COPY ./requirements/python ./requirements/python
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/python/requirements.txt -r requirements/python/dev_requirements.txt

COPY . .

RUN pip3 install -e .
