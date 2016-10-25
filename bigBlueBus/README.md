Below are the steps to run this host on a AWS Ubuntu instance. Note there should be an RDS instance created already with a database called "sample" and a user named "tutorial_user"

    1  sudo apt-get update

    2  sudo apt-get upgrade

    3  sudo apt-get install python-pip

    4  sudo apt-get install python-dev

    5  sudo apt-get install build-essential

    6  sudo chmod 4777 /usr/local/lib/python2.7/dist-packages/

    7  sudo chmod 777 /usr/local/bin

    8  pip install virtualenvwrapper

    9  mkdir django

   10  cd django/

   11  virtualenv vp27

   12  source vp27/bin/activate

   13  pip install django

   14  sudo apt-get install python-psycopg2

   15  sudo apt-get install libpq-dev

   16  pip install psycopg2

   17  django-admin.py startproject myproject .

   18  cd myproject/

   20  cp settings.py settings.py.bak

   21  vi settings.py

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'sample',

        'USER': 'tutorial_user',

        'PASSWORD': '********',

        'HOST': '***', 

   22  python manage.py makemigrations

   29  sudo apt-get postgresql postgresql-contrib

   30  sudo apt-get install postgresql postgresql-contrib

   32  sudo su - postgres

   31  psql

   39  python manage.py makemigrations

   40  python manage.py migrate

   41  python manage.py createsuperuser

   46  psql -h tutorial-db-instance.chsrghcqrg5j.us-west-1.rds.amazonaws.com -U tutorial_user sample

   50  python manage.py runserver 0.0.0.0:8000

import BBB data
---------------

   88  python manage.py makemigrations api

   90  python manage.py sqlmigrate api 0001

   91  python manage.py migrate

   96  mkdir bbb_data

   97  cd bbb_data

   99  curl http://gtfs.bigbluebus.com/parsed/stops.txt > stops.txt

  100  curl http://gtfs.bigbluebus.com/parsed/routes.txt > routes.txt

  101  curl http://gtfs.bigbluebus.com/parsed/trips.txt > trips.txt

  102  curl http://gtfs.bigbluebus.com/parsed/stop_times.txt > stop_times.txt

105 psql -h tutorial-db-instance.chsrghcqrg5j.us-west-1.rds.amazonaws.com -U tutorial_user sample

\copy api_routes (route_id, agency_id, route_short_name, route_long_name, route_desc, route_type, route_url, route_color, route_text_color) from '/home/ubuntu/bbb_data/routes.txt' with delimiter ',' CSV header;

\copy api_trips (stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,stop_timezone,wheelchair_boarding) from '/home/ubuntu/bbb_data/stops.txt' with delimiter ',' CSV header;

\copy api_stops (stop_id,stop_code,stop_name,stop_desc,latitude,longitude,stop_zone,stop_url,stop_location_type,parent_station,timezone,wheelchair) from '/home/ubuntu/bbb_data/stops.txt' with delimiter ',' CSV header;

\copy api_stoptimes (trip_id, arrival_time, departure_time, stop_id, stop_sequence, stop_headsign, pickup_type, drop_off_type, shape_dist_traveled, timepoint) from '/home/ubuntu/bbb_data/stop_times.txt' with delimiter ',' CSV header;

build the rest api
-------------------
set up file serailizers.py from my github:

   146  pip install djangorestframework

   157  pip install django-cors-headers

set up nginx:
=============

  317  sudo apt-get install nginx
  318  sudo service nginx start
test out web page
  319  sudo service nginx stop
  321  sudo vim /etc/nginx/sites-enabled/default
#root /usr/share/nginx/html;
root /home/ubuntu/www;
  322  sudo service nginx start
  329  cd
  330  mkdir www
  330  cd www
  331  vi index.html

set up web page:
================
       mkdir ~/git
  348  cd git
  349  git clone https://github.com/slarribeau/www.git
  350  cp www/google/bbb.html ~/www/
  351  cp www/google/bus_logo.png ~/www/
  352  mv ~/www/bbb.html ~/www/index.html
  354  cp ../git/www/google/mystyle.css ~/www

