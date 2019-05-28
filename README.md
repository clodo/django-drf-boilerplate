Django DRF Boilerplate
############

Boilerplate with Django, DRF and authentication. 

Requirements
============

* Python >= 3.5
* Django >= 2.1


Installation
============

1. Create a .env file in root folder:

* Use .env.template

* Update variables according to your needs

2. Ubuntu dependencies

.. code-block:: bash

    $ sudo apt install python3-dev

2. Install (dev) requirements:

.. code-block:: bash

    $ pip install -r requirements/local.txt

3. Run migrations:

.. code-block:: bash

    $ python manage.py migrate

4. Create superuser

.. code-block:: bash

    $ python manage.py createsuperuser --email claudiobidau@gmail.com

5. Run tests:

.. code-block:: bash

    $ python manage.py test --settings=config.settings.test

6. Run server:

.. code-block:: bash

    $ python manage.py runserver

7. Code coverage:

.. code-block:: bash

    $ coverage run --source='project/api' manage.py test --settings=config.settings.test

    $ coverage report