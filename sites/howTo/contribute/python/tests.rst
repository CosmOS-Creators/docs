Tests
=============================

This page will describe how to contribute with unit tests for the python code base. We strongly suggest using the VSCode development environment running in the docker container.

Test folder structure in a module folder
------------------------------------------
The folder structure for python unit tests is fairly simple. The tests should be placed in a folder named :file:`tests` which is a subfolder of the module it is testing.
Inside that :file:`tests` folder a file named :file:`__init__.py` has to be created to enable proper import handling.
Also inside the :file:`tests` folder one can create as many test python files as desired. The only important thing is that the name of these files start with ``test_``.
After the underscore a descriptive name for the test suite should follow.
If any additional config files are needed for the unit tests a subfolder with a descriptive name should be created inside the :file:`tests` folder. Referring to those files from the test cases should be done only using relative paths.

Newly implemented unit test should use the class syntax of pytest to define their test suite and the unit tests inside of that.

In the end the folder structure for one unit might look similar to this example:
    ::

        Parser (module)
        ├── __init__.py
        ├── source_code.py
        ├── more_source_code.py
        └── tests
            ├── __init__.py
            ├── test_something.py
            └── test_configs
                └── config.json

Naming conventions
--------------------
#. Unit test files inside the :file:`tests` folder are usually named after the source file that they are testing.
   For example tests for a class inside the source file :file:`Serializer.py` should be named :file:`test_Serializer.py`.
#. Names of the test clases and test methods should follow the naming conventions of the
   `tests outside of application code from pytest <https://docs.pytest.org/en/6.2.x/goodpractices.html#tests-outside-application-code>`_ and
   the `grouping of tests in a class <https://docs.pytest.org/en/6.2.x/getting-started.html#group-multiple-tests-in-a-class>`_.

Implementation
----------------
Nothing too much to mention here other than thinking a bit about the test cases, following the usual arrange-act-assert structure of unit tests and considering
to set up some shared setup functions where it makes sense to not duplicate any code. Those could be put into a separate python file (which does not start with ``test_``)
which can then easily be imported into any unit test file that needs one of these common setup functions.


Tips and tricks
-----------------
#. If you develop in VSCode you can use the testing sidebar for auto discovering your testcases and even execute and check the status of particular ones using the inline run button:

   .. image:: ../../../../images/pyUnitTests/testing_shortcuts_in_the_code.png
