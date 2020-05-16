# Start with a Python image.
FROM python:3

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1


# Copy all our files into the image.
RUN mkdir /django
RUN mkdir /django/tools
WORKDIR /django
ADD requirements.txt /django/

# Install our requirements.
RUN pip install -r requirements.txt
ADD tools /django/tools/

# Install vim
RUN apt-get update -y
RUN apt-get install gdal-bin libgdal-dev vim  -y --no-install-recommends
