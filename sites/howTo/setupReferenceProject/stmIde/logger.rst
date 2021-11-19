Logger
=============================

This page will provide you with information about the logger and serial port connection creation in the STM32 Cube IDE.

Prerequisites
--------------

- Flashed reference hardware development board with the reference project image with logger testing program.

New serial port connection creation
----------------------------------------

#. First of all we open the STM32 Cube IDE and on the bottom right side we expand the :menuselection:`Window+ icon (New console)` option and select :menuselection:`Command Shell Console`.
    .. image:: ../../../../images/logger/command_shell.png
        :alt: Command shell opening
#. New window will show up with the name *Select Remote Connection*. Now we have to create a new connection name and therefore we click on the **New** button next to the select connection.
    .. image:: ../../../../images/logger/select_connection.png
        :alt: Choose project directory
#. Another window will show up with the name *New Serial Port Connection*. We set it up exactly as it is shown in the picture except the serial port which should be configured based on your local connection.
    .. image:: ../../../../images/logger/logger_creation.png
        :alt: Serial port connection creation
#. If the serial port connection creation was successful we will see the logger output at the bottom of the STM32 Cube IDE.
    .. image:: ../../../../images/logger/logger_output.PNG
        :alt: Logger output.
