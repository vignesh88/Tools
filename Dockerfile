# Start with a Python image.
FROM python:3

# port exposed
EXPOSE 8001

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
COPY .env.example /django/tools/.env
COPY . /django/tools/


# Install vim
RUN apt-get update -y
RUN apt-get install gdal-bin libgdal-dev vim  -y --no-install-recommends

# command executed at run
CMD ["python", "tools/manage.py", "runserver", "0.0.0.0:8001"]
