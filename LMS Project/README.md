# Moodle Alternative, SEM VI

## Development


#### Prerequsites

Check that you have installed following:

* Python >= 3.5
* [PIP](https://pypi.python.org/pypi)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)

_Make sure PIP and Virtualenv are installed for proper version of Python
(if you have installed more than one version of Python)._

If you never worked with Virtualenv before, go to
https://virtualenv.pypa.io/en/stable/ and read concept about it.

#### Getting started

After you clone repo to your local computer, navigate to newly created
directory and do the following steps:

1. Create Virtualenv

   ```
   $ virtualenv env
   ```

   This will create `env` directory inside project. Don't worry,
   it's ignored by GIT by default.

2. Activate Virtualenv for the project

   ```
   $ source ./env/bin/activate
   ```

   This will activate local development environment in current terminal
   session only. You have to run this command for every new terminal session.

   You should notice `(env)` text at the beginning of your command line prompt.

3. Install requirements
   ```
   (env) $ pip install -r requirements.txt
   ```

4. Run migrations in order to create db and tables

   ```
   (env) $ python manage.py db upgrade
   ```

5. Run server

   ```
   (env) $ python manage.py runserver
   ```

6. Open web-browser and navigate to [http://localhost:5000](http://localhost:5000)


## Documentation

All documentation can be found in [doc](doc/README.md) directory.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) file.
