World API
=========

Running the app
---------------

-  Copy the ``.env.example`` to ``.env`` and populate it with the proper
   environment variables.
-  Run the ``scripts/gen_initsql.py`` script. Either run it with
   ``pipenv``:

.. code:: shell

   pipenv run python scripts/gen_initsql.py

or load the ``.env`` environment file (through ``autoenv``, or simply
just source it) and then run the script with your python interpreter.
Check if ``scripts/init.sql`` was created with the proper secrets
populated.

-  Start the containers:

.. code:: shell

   docker-compose up --force-recreate --build

-  You should have the app running on port 8080. Try hitting the
   ``/cities`` endpoint for example:

.. code:: shell

   curl -X GET http://localhost:8080/cities

You may use whatever tool you like (``http`` from ``httpie`` for
example), or you can run the Postman collection from ``tests/postman``.
