Empty Python Project Template
=============================

This template provides a basic template for a Python project, with
out-of-the-box support for py.test_, coverage_, Sphinx_, tox_, and
the standard Python flow for `building`_ and `distributing`_ projects.

An .editorconfig_ file is provided to ensure standard settings when 
working with multiple editors.

A travis.yml_ file is provided for easy integration with the travis_
CI system, which is free for open-source projects.

The default license included in the ``LICENSE`` file is the `MIT license`_.

Features
--------

* Sphinx automatically parses the package name and version number, so there
  is no need to edit ``conf.py`` for most projects
* ``CHANGELOG.rst`` and ``README.rst`` are automatically included as the
  homepage of the Sphinx-generated documentation
* ``setup.py`` automatically parses ``requirements.txt`` for requirements and
  the package version, so there is no need to update in multiple places
* tox_ is configured by default to build the project documentation using
  Sphinx and autodoc, so all of your docstrings will be automatically
  documented

Getting Started
---------------

To get up and running, first check out the repo locally and copy it into your
project root:

.. code:: bash

    mkdir my_project
    git clone https://github.com/mplanchard/python_skeleton
    cp -r python_skeleton/* my_project/
    cp python_skeleton/.editorconfig my_project/
    cp python_skeleton/.gitignore my_project/
    cd my_project

Then setup and activate a virtual environment for the project. A 
``create_venv.sh`` script is provided for convenience. Note that the provided
script assumes you want to use "python3" as an interpreter. If you don't,
adjust the script to use your desired Python prior to running the following
commands:

.. code:: bash

    ./create_venv.sh
    source venv/bin/activate

Then adjust the following as needed:

* Rename the ``package_name`` directory to your desired package name
* Fill in the constants in ``setup.py``, ensuring that ``NAME`` matches the
  directory name of your package
* Assign your package name to the ``PACKAGE_NAME`` environment variables
  in ``tox.ini``
* If you don't want to support Python 2 (a more and more reasonable decision),
  remove ``py27`` from the environments list in ``tox.ini``, and then in
  ``setup.cfg``, comment out ``universal=1`` and uncomment ``python-tag=py3``.
* If you're using type-hints and you intend to support anything less than 
  Python 3.5, uncomment the indicated line in ``requirements.txt``

You should now be able to:

* Install your package in development mode:

  .. code:: bash

    pip install -e .

* Run tests

  .. code:: bash

    py.test

* Run tests against all configured Python interpreters and build documentation

  .. code:: bash

    tox

* Build your project

  .. code:: bash

    python setup.py bdist_wheel


Contributing
------------

I use this repo as a skeleton for the majority of my projects, and you are
welcome to do the same. If you'd like to fix something, improve the
documentation, or add a new feature, please feel free to open a PR_. If there's
a feature you'd like to see added and you're unsure of how to contribute,
raise an Issue_.

.. _py.test: https://docs.pytest.org/en/latest/
.. _coverage: https://coverage.readthedocs.io/
.. _sphinx: http://www.sphinx-doc.org/en/stable/index.html
.. _tox: https://tox.readthedocs.io/en/latest/
.. _building: http://setuptools.readthedocs.io/en/latest/setuptools.html
.. _distributing: https://packaging.python.org/distributing/
.. _.editorconfig: http://editorconfig.org/
.. _travis.yml: https://docs.travis-ci.com/user/languages/python/
.. _travis: https://docs.travis-ci.com/
.. _`mit license`: https://en.wikipedia.org/wiki/MIT_License
.. _pr: https://github.com/mplanchard/python_skeleton/pulls
.. _issue: https://github.com/mplanchard/python_skeleton/issues

