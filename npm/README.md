# Vikki's Tools

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/62d245757a5d4a8e97b2174dc9a56406)](https://app.codacy.com/manual/vignesh88/tools?utm_source=github.com&utm_medium=referral&utm_content=vignesh88/tools&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/vignesh88/Tools.svg?branch=master)](https://travis-ci.org/vignesh88/Tools)
[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/vikki/Vikki's%20tools%2FVikki's%20tools?key=eyJhbGciOiJIUzI1NiJ9.NWVjMGU3ZTU2MTllYjZmNTYxYTRjYWIy.fSVMhnKfcSepXilVqCA1AY7vocNQ6s3Xkm-pSKB4zt4&type=cf-1)]( https%3A%2F%2Fg.codefresh.io%2Fpipelines%2FVikki's%20tools%2Fbuilds%3Ffilter%3Dtrigger%3Abuild~Build%3Bpipeline%3A5ec0ed5b1350575c3a125e3f~Vikki's%20tools)
[![Website tools.vikki.in](https://img.shields.io/website-up-down-green-red/https/tools.vikki.in.svg)](https://tools.vikki.in)
![Uptime Robot status](https://img.shields.io/uptimerobot/status/m784955377-01831883b9c483057e013bf9)
![Uptime Robot ratio (30 days)](https://badgen.net/uptime-robot/month/m784955377-01831883b9c483057e013bf9)
![(last hour) response](https://badgen.net/uptime-robot/response/m784955377-01831883b9c483057e013bf9)

### To generate a new secreat key for django

```
#python manage.py shell
In [1]: from django.core.management.utils import get_random_secret_key
In [2]: get_random_secret_key()
Out[2]: '555%s(xc)a4-^x*3ipd@_@z81n_mry#flyx9@boy0b@jeg_4ao'

```

### Installation

```
#git clone https://github.com/vignesh88/tools.git
#cd tools/
#python manage.py migrate --run-syncdb
#python manage.py runserver 0.0.0.0:8086
```

### Alternate installation using docker

```
#sudo docker run -d -p 8086:8086 --name tools.vikki.in vignesh88/tools python tools/manage.py runserver 0.0.0.0:8086
```

> Open your browser and view the application at [http://localhost:8086](http://localhost:8086)

## Tools available

- URL Shortner
- Password generator
- Base64 converter
- Epoch timestamp converter
- What is my IP

### URL Shortner

A simple django based tool to create a short URL based on [hashid](https://hashids.org/) algorithm.
The short domain is in the format s.vikki.in/[yourhashid].
The statistic of short URL will be available in s.vikki.in/[yourhashid]/stats

### Password generator

A simple tool to generate random password. This tools also has the advantage of using the custom words in password which uses python nltk wordnet library.

### Base64 encoder and decoder

A simple tool to encode and decode a base64 string

### Epoch converter

A simple tool to conver epoch to datetime format and from datetime to epoch format

### What is my IP Address

A simple tool to view your public IP address

### License

GNU General Public License v3.0 - read the LICENSE file for details.