Studio Docs
===========

What is this?
-------------

This is the repository where user documentation for `Kolibri Studio <https://studio.learningequality.org/>`__ is maintained. To read the documentation visit `kolibri-studio.readthedocs.io <https://kolibri-studio.readthedocs.io/>`__.


Building the docs locally
-------------------------

You will need an environment with `make <https://en.wikipedia.org/wiki/Make_(software)>`__

.. code-block:: bash

  # Create a Python 3 virtual environment using Virtualenvwrapper
  # See: https://virtualenvwrapper.readthedocs.io/
  mkvirtualenv -p python3 kolibri-docs

  # Install Python requirements
  pip install -r requirements.txt


Build and run:

.. code-block:: bash

  make docs

You should now be able open the built docs with a web browser at ``docs/_build/html/index.html``.

You can also have the docs automatically build and reload:

.. code-block:: bash

  sphinx-autobuild docs docs/_build/html


You should now be able open the automatically-rebuilding docs with a web browser at ``http://127.0.0.1:8000``.



License
-------

.. image:: https://i.creativecommons.org/l/by-sa/4.0/88x31.png
   :alt: Creative Commons License

This work is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`__
