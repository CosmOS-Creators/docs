.. |PYTHON_DIRECTORY| replace:: :file:`Cosmos/customBox/python`


Functional
=============================

This page will describe how to contribute to the CosmOS Python code base. We strongly suggest using the VSCode development environment running in the docker container.

Folder structure
--------------------
All Python modules are contained inside the python subdirectory in the customBox repository (|PYTHON_DIRECTORY|).
Modules are allowed to have submodules and everything follows the usual Python structures and rules.

Python files that are located in the root of the python directory are considered project specific. Modules could be project specific as well, the Model module is such a case.
In general there should always be a clear split between project specific and generic code.

Unit tests are always located inside the module they belong in a subdirectory called :file:`tests`. These subdirectories are automatically discovered by `pytest <https://docs.pytest.org/>`_ so no there is no need to add them manually.

Naming conventions and code styling
-----------------------------------
All naming conventions and code should follow the `PEP 8 Style Guide <https://www.python.org/dev/peps/pep-0008/>`_

Code should be written and structured in such a way that no modification to the ``PYTHONPAH`` environment variable is required.
If you are using VSCode with the provided configuration it should already be setup to add the |PYTHON_DIRECTORY| path to the ``PYTHONPAH``
