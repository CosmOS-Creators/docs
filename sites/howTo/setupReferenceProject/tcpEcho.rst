TCP Echo
=============================

This page will provide you information about TCP echo test using command line echo server and client for Windows.
It is possible to use any other tool to get the same results as shown in this specific demo.

Prerequisites
--------------

- Flashed reference hardware development board with the reference project image with echo server testing program.
- `Echo tool <https://github.com/PavelBansky/EchoTool>`_\
- Currently is the reference project lwip stack IP address configured as static 192.168.1.30, this is of course possible to change to match your local network configuration.

TCP echo test between windows host and reference hardware
------------------------------------------------------------------

#. If we are using echotool on the windows host machine we open windows command prompt and compose command shown below.
    .. code-block::

            <echotool.exe path> <server IP> /p tcp /d <test message>
#. It is possible to open logger before sending echo to the reference hardware from host machine to see if the echo was received by the echo server program running on the reference hardware.
#. After the echo is send (in this case with echotool), with opened logger serial port connection we can see also the log message telling us wich IP address sent the echo and what was the echo message as it is shown in the picture below.
    .. image:: ../../../images/tcpEcho/tcp_echo.png
        :alt: TCP echo with logger
