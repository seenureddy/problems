# Galle Test

## Setup development environment ##

Just execute these commands in your virtualenv(wrapper):

We need to setup some environment varaibles in the activate script.

```
export DATABASE_URL=postgres://username:password@host:port/databasename

for ex:
 export DATABASE_URL="postgres://seenu:123456@localhost:5432/galledb"

If you don't setup the database in virtual environment. It will use
the default sqlite3 database.
```

```
pip install -r requirements/development.txt
python manage.py migrate --noinput
python manage.py runserver
```

If you are not using the postgres then `don't use the regenrate script to
create database`.

** Search functionality we require the postgres install

```
sudo aptitude install postgresql-9.5 postgresql-server-dev-9.5 postgresql-client-9.5
postgresql-server-dev-9.5
```

After installing the requirement user this script to generate the database.
```
./regenerate.sh
```
