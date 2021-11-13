Hardware
=============================

This page will introduce the reference hardware used in the CosmOS reference project.

MCU
--------------
As the reference microcontroller we chose dual core STM32H755ZI. This microcontroller is based on the two 32-bit RISC Arm® cores,
the Cortex®-M7 and Cortex®-M4.

The main features are:
~~~~~~~~~~~~~~~~~~~~~~
* FPU single- and double-precision (Cortex®-M7 core)
* MPU
* L1 cache: 16 Kbytes of data and 16 Kbytes of instruction cache (Cortex®-M7 core)
* 2 Mbytes of Flash memory with read-while-write support
* 1 Mbyte of RAM
* Ethernet MAC interface with DMA controller

and more you can read on the `STM32H755ZI microcontroller product page <https://www.st.com/en/microcontrollers-microprocessors/stm32h755zi.html/>`_


Development board
------------------
As the reference development board we chose Nucleo-144 development board with STM32H755ZI MCU.

The main features are:
~~~~~~~~~~~~~~~~~~~~~~
* USB OTG full speed or device only
* Board connectors:USB with Micro-AB or USB Type-C®Ethernet RJ45
* On-board ST-LINK debugger/programmer with USB re-enumeration capability: mass storage, Virtual COM port, and debug port
* Support of a wide choice of Integrated Development Environments (IDEs) including IAR Embedded Workbench®, MDK-ARM, and STM32CubeIDE

and more you can read on the `Nucleo-144 board product page <https://www.st.com/en/microcontrollers-microprocessors/stm32h755zi.html/>`_


Resources
--------------

- `STM32H755ZI microcontroller product page <https://www.st.com/en/microcontrollers-microprocessors/stm32h755zi.html>`_
- `STM32H755ZI MCU reference manual <https://www.st.com/resource/en/reference_manual/dm00176879-stm32h745755-and-stm32h747757-advanced-armbased-32bit-mcus-stmicroelectronics.pdf>`_
- `Nucleo-144 board product page <https://www.st.com/en/microcontrollers-microprocessors/stm32h755zi.html>`_
- `H755ZIQ-C01 development board schematics <https://www.st.com/resource/en/schematic_pack/mb1363-h755ziq-c01_schematic.pdf>`_
