==============
python_modules
==============
This is an experiment to make Python virtual environments created by the Python
`venv` module behave like `Node.js`_ npm environments.

Installation
------------
The virtual environment autoloader is executed via the
`usercustomize`_ module being
placed the users site-packages.

Run the following commands to install the autoloader hook:

.. code-block:: shell

  mkdir -p $(python -m site --user-site)
  curl https://raw.githubusercontent.com/wesclemens/python_modules/master/usercustomize.py > $(python -m site --user-site)/usercustomize.py

Initialize Virtual Environments
-------------------------------
.. code-block:: shell

  cd <my_project>
  python -m venv python_modules

Any python command ran from `<my_project>` directory will use `python_modules`
as its site-packages.

.. _usercustomize: https://docs.python.org/3.6/library/site.html
.. _Node.js: https://nodejs.org
