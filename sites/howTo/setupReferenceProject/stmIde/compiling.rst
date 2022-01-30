Compiling
=============================

This page will provide you with information about compiling of the reference project in the STM32 Cube IDE.

Prerequisites
--------------

- Imported reference project into the STM32 Cube IDE.


Compiling of the reference project
----------------------------------------

#. To compile a single core we have to highlight one of the cores under the project root and expand the :menuselection:`Hammer icon (Build)` option in the menu and choose :menuselection:`Debug` to build.
    .. image:: ../../../../images/stmIde/compiling_debug.png
        :alt: Compiling of the core CM4
#. After the compilation process has successfully finished we can see the memory consumption data for all configured partitions in the *Build Analyzer* window of the STM32 Cube IDE.
    .. image:: ../../../../images/stmIde/memory_usage.PNG
        :alt: Memory usage
#. For a detailed view of the data/code mapped to each memory partition we can switch to the **Memory Details** tab.
    .. image:: ../../../../images/stmIde/memory_details.PNG
        :alt: Memory details
