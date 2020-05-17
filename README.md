# Vikki's Tools
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/62d245757a5d4a8e97b2174dc9a56406)](https://app.codacy.com/manual/vignesh88/tools?utm_source=github.com&utm_medium=referral&utm_content=vignesh88/tools&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/vignesh88/Tools.svg?branch=master)](https://travis-ci.org/vignesh88/Tools)

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
#python manage.py runserver 0.0.0.0:8086
```

### Alternate installation using docker
```
#sudo docker run -d -p 8086:8086 --name vikki_tools vignesh88/tools python epoch/manage.py runserver 0.0.0.0:8086
```

### External libraries used

Javascript
----------
- [superplaceholder](https://github.com/chinchang/superplaceholder.js)
- [JS Cookie](https://github.com/js-cookie/js-cookie)
- bootstrap.bundle.min
- jquery.min.js
- darkmode-js.min.js
- moment.min.js
- moment-timezone.js
- moment-timezone-with-data-2012-2022.js
- chosen.jquery.js
- jstz.min.js
- bootstrap.bundle.min.js

CSS
-------
- bootstrap.min.css
- simple-sidebar.css
- bootstrap-datetimepicker.min.css
- bootstrap-datetimepicker.min.js
- bootstrap-select.min.css
- bootstrap-select.min.js