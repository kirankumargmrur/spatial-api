FROM osgeo/gdal:ubuntu-full-3.3.1
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.8
RUN ln -sf /usr/lib/python3/dist-packages/apt_pkg.so \
    /usr/lib/python3/dist-packages/apt_pkg.cpython-36m-x86_64-linux-gnu.so
RUN apt-get install -y python3-pip libpq-dev python-dev python3-setuptools
RUN python3 -m pip install pip
RUN python3 -m pip install setuptools-rust
RUN apt-get update
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common postgresql-client
ENV export CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV PYTHONUNBUFFERED 1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
