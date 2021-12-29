Pre-alpha
=============================

Overview
-----------
The pre-alpha version of the CosmOS project is the **first public release**. The main idea
of the pre-alpha release is to **open project for the contributors**. As we initially worked in the
very small group composed of two developers, the publicly released project can help us to get a different
opinions, ideas and overall perspective, as we strive to enhance the overall quality and safety of the
software within the future releases.


What does pre-alpha contain?
---------------------------------
- CosmOS whitepaper describe the ideas behind the CosmOS project and we strongly suggest reading it to get better overview about the motivation, architecture and technical concepts.
- `Docker dev environment <https://github.com/CosmOS-Creators/dev_environment>`_ provided for easier project setup.
- Working `reference integration <https://github.com/CosmOS-Creators/reference_project_stmIDE>`_ on the STM32H755ZI dual-core microcontroller with the STM32 IDE.
- `CustomBox GUI <https://github.com/CosmOS-Creators/customBox>`_ supports configuration and code generation.
- `Multiple example programs, tasks and threads configured <https://github.com/CosmOS-Creators/reference_project_stmIDE/tree/master/Cosmos/generated/application/src>`_ with **channels, buffers, system jobs, mutexes, semaphores, spinlocks, peripheral accesses, thread sleep and dynamic allocations** implemented.
- `C unit tests <https://github.com/CosmOS-Creators/core/blob/master/core/test/ut/core/ut.cpp>`_ implemented to provide working reference for the future contributions.
- `Python tests <https://github.com/CosmOS-Creators/customBox/blob/master/python/Parser/tests/test_AttributeTypes.py>`_ implemented to provide working reference for the future contributions.
- C code documented by doxygen comments and generated in the CosmOS GitHub pages.
- GitHub pages provide a lot of information for the people who want to contribute or just to try out the project.
