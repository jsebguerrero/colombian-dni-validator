FROM tiangolo/uvicorn-gunicorn:python3.7
MAINTAINER Juan S. Guerrero <jsebastian.guerrero@udea.edu.co>

RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    cmake \
    git \
    unzip \
    pkg-config \
    python-dev \
    python-opencv \
    libopencv-dev \
    ffmpeg  \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libgtk2.0-dev \
    python-numpy \
    python-pycurl \
    libatlas-base-dev \
    gfortran \
    webp \
    python-opencv \
    qt5-default \
    libvtk6-dev \
    zlib1g-dev

RUN apt-get update && apt-get install -y libleptonica-dev \
    tesseract-ocr libtesseract-dev \
    libtesseract-dev
RUN apt-get install -y python3-dev


COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8
EXPOSE 9001
CMD ["python3", "run.py"]
