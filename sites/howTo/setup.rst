Setup development environment
=============================

This page will describe how to setup the development environment for developing/contribution on the CosmOS reference project.
The guide will focus on installing the environment on a windows system but since we are
using docker containers and VSCode it should work on most operating systems.

Prerequisites
--------------

- Windows with at least `WSL2 <https://docs.microsoft.com/en-us/windows/wsl/install>`_ installed or just linux will work too.
- `Docker <https://docs.docker.com/desktop/windows/wsl/>`_
- `Visual Studio Code <https://code.visualstudio.com/>`_

First time code checkout
------------------------

#. Clone the `dev environment repository <https://github.com/CosmOS-Creators/dev_environment>`_ by either downloading the zip from github or using this git command:
    .. code-block::

            git clone https://github.com/CosmOS-Creators/dev_environment.git
#. Open the VSCode workspace.
#. Install the recommended VSCode plugins.
#. You now have two choices:
    #. Run with GUI support:
        - If you want to also run any graphical applications (like CustomBox) from the docker container make sure that you have `WSLg <https://github.com/microsoft/wslg>`_ installed if you are on windows.
        - Open the file :file:`.devcontainer/dev_container_GUI.yaml`
        - If you are on windows make sure that under volumes the path on the left of the ``:`` symbol matches your particular installed WSL distro.
          The default one is set to ``Ubuntu-20.04``

          If you are on linux you should be able to just mount it to the same location as it is mounted to inside the container.
    #. Run without GUI support:
        - Open the file :file:`.devcontainer/devcontainer.json` and make sure that the property ``dockerComposeFile`` is set to use the :file:`dev_container.yaml` file
#. VSCode should ask you now if you would like to reopen the workspace in a new docker container. Select reopen in container:
    .. image:: ../../images/open_in_container_message.png
        :alt: Reopen in container message
#. After VSCode reopens open a new terminal window and run the following command:
    .. code-block::

            git clone https://github.com/CosmOS-Creators/reference_project_stmIDE.git . --recurse-submodules
#. Now you might need to select workspace folder location inside the docker container in VSCode or you can also just close and reopen VSCode in order for it to to it for you.


Compiling the source code
-------------------------

Some default build commands have been setup ready to use in VSCode.
You just need to press :kbd:`Ctrl+Shift+B` to call the default build task.
