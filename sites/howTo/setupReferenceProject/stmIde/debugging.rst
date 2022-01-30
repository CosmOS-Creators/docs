Debugging
=============================

This page will provide you with information about compiling of the reference project in the STM32 Cube IDE.

Prerequisites
--------------

- Successfully compiled reference project source code for both cores with the STM32 Cube IDE.


STM32 Cube IDE multi-core debugging
----------------------------------------

#. First of all we have to launch the already configured debug launch group. To do so we open the STM32 Cube IDE and expand the :menuselection:`Bug icon (Debug)` option. We can see multiple options for debugging single cores, but in our case we choose the **Launch Group** option with the name :menuselection:`reference_project_stmIDE`.
    .. image:: ../../../../images/stmIde/start_debug.png
        :alt: Launch debug group
#. After the debug group launch the *Switch Perspective* window will show up. We click on the **Switch** option to use the debug perspective.
    .. image:: ../../../../images/stmIde/debug_perspective_switch.png
        :alt: Switch perspective
#. In the debug perspective we can see both cores (CM4/CM7), if not please wait till the code has been flashed. We can now start the cores one by one. We start with the CM4, click on the core in the debug explorer and then click on the :menuselection:`Play icon (Run)` in the menu.
    .. image:: ../../../../images/stmIde/run_cores.png
        :alt: Run cores
#. If we did everything correctly we should see that both cores are in a *Running* state.
    .. image:: ../../../../images/stmIde/running_cores.PNG
        :alt: Running cores

References
--------------

- `STM32 Cube IDE ST-LINK GDB server <https://www.st.com/resource/en/user_manual/um2576-stm32cubeide-stlink-gdb-server-stmicroelectronics.pdf>`_
- `STM32 Cube IDE multi-core debugging <https://www.st.com/resource/en/application_note/dm00629855-getting-started-with-projects-based-on-dualcore-stm32h7-microcontrollers-in-stm32cubeide-stmicroelectronics.pdf>`_
