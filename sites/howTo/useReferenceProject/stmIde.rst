STM32 Cube IDE project import
=================================

Reference project uses STM32 Cube IDE project structure, and it is possible to open, compile and debug in it.
This page will provide you information about import of reference project into the STM32 Cube IDE.

Prerequisites
--------------

- Locally cloned `reference project repository <https://github.com/CosmOS-Creators/reference_project_stmIDE>`_
- `STM32 Cube IDE <https://www.st.com/en/development-tools/stm32cubeide.html>`_


First time STM32 Cube IDE project import
----------------------------------------

#. First of all we open the STM32 Cube IDE and go to the menu option File/Open projects from file system.
    .. image:: ../../../images/stmIde/import_project_stmIde.png
        :alt: Open projects from file system
#. Then a window *Import project from the file system or archive* will show up and we click on the highlighted button **Directory**. The file explorer window will show up and we point to the reference project directory and press button **Select Folder**.
    .. image:: ../../../images/stmIde/choose_directory_import.png
        :alt: Choose project directory
#. After this point we just click on the button **Finish** and STM32 Cube IDE will import the whole nested project structure.
    .. image:: ../../../images/stmIde/finish_import.png
        :alt: Finish import
#. If the project import was successful we will see the reference_project_stmIDE in the Project Explorer on the left side of STM32 Cube IDE.
    .. image:: ../../../images/stmIde/imported_project.PNG
        :alt: Imported project
#. In the end we have to ensure that the projects for the both cores are converted to the C++ language. We highlight the core one by one and check if there is option to convert it to C++, if not it was already done.
    .. image:: ../../../images/stmIde/convertToCpp.png
        :alt: Convert project to C++
