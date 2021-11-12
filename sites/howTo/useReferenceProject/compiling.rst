Compiling
=============================

This page will provide you information about compiling of the reference project in the STM32 Cube IDE.

Prerequisites
--------------

- Imported reference project into the STM32 Cube IDE.


Compiling of the reference project
----------------------------------------

#. To compile one of the cores we have to highlight one of the cores under the project root and expand the hammer (build) option in the menu to choose debug build.
    .. image:: ../../../images/stmIde/compiling_debug.png
        :alt: Compiling of the core CM4
#. After the compilation process is successfully finished we can see on the right side of STM32 Cube IDE in build analyzer window memory consumption data for all configured partitions.
    .. image:: ../../../images/stmIde/memory_usage.PNG
        :alt: Memory usage
#. For the detailed view of the data/code mapped to each memory partition we can switch to the **Memory details** tab.
    .. image:: ../../../images/stmIde/memory_details.PNG
        :alt: Memory details
