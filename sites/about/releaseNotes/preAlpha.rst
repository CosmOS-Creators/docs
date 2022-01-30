Pre-alpha
=============================

Overview
-----------
The pre-alpha version of the CosmOS project is the **first public release**. The main idea
of the pre-alpha release is to **open project for the contributors**. As we initially worked in a
very small group composed of two developers :) , the publicly released project can help us to get different
opinions, ideas and overall perspective, as we strive to enhance the overall quality and safety of the
software with future releases.

What features does the pre-alpha offer?
----------------------------------------
- CustomBox GUI supports configuration and generation.
- Support for multi-core microcontrollers.
- Hybrid scheduling combines the complex real-time non-preemptive scheduling and multi-threaded preemptive scheduling.
- Memory mapping and memory protection of tasks/threads stacks, user program heaps, and user program data.
- Memory manager supports thread-safe dynamic allocations.
- Inter-program safe data transfers.
- Configurable tasks/threads permissions for data transfers.
- Possibility to implement drivers in the application layer with configurable peripheral access.
- Modular kernel expansion by system jobs with inner scheduling.
- Configurable synchronization primitives - spinlocks, semaphores and mutexes.
- Highly portable and modular design, which is easy to port and expand.

What does pre-alpha contain?
---------------------------------
- The CosmOS whitepaper describes the ideas behind the CosmOS project and we strongly suggest reading it to get a better overview about the motivation, architecture and technical concepts.
- `Docker dev environment <https://github.com/CosmOS-Creators/dev_environment>`_ provided for easier project setup.
- Functional `reference integration <https://github.com/CosmOS-Creators/reference_project_stmIDE>`_ on the STM32H755ZI dual-core microcontroller with the STM32 IDE.
- Functional `customBox GUI <https://github.com/CosmOS-Creators/customBox>`_ which can be used for configuration and code generation.
- `Multiple example programs, tasks and threads configured <https://github.com/CosmOS-Creators/reference_project_stmIDE/tree/master/Cosmos/generated/application/src>`_ with **channels, buffers, system jobs, mutexes, semaphores, spinlocks, peripheral accesses, thread sleep and dynamic allocations** implemented.
- `C unit tests <https://github.com/CosmOS-Creators/core/blob/master/core/test/ut/core/ut.cpp>`_ implemented to provide a functional reference for the future contributions.
- `Python tests <https://github.com/CosmOS-Creators/customBox/blob/master/python/Parser/tests/test_AttributeTypes.py>`_ implemented to functional working reference for the future contributions.
- C code documented by doxygen comments and generated in the CosmOS GitHub pages.
- GitHub pages providing a lot of information for the people who want to contribute or just to try out the project.
