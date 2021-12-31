Structure
=============================
This page will introduce the structure of the CosmOS reference project.

The reference project uses STM IDE project structure, and it is possible to open, compile and debug in it.
    ::

        reference project
        ├── CM4
        ├── CM7
        ├── Common
        ├── Cosmos
        ├── Drivers
        ├── Middlewares
        ├── .mxproject
        ├── .project
        └── reference_project_stmIDE.ioc

Under the Cosmos directory we can found following structure:
    ::

        reference project/Cosmos
        ├── build
        ├── configuration
        ├── core (submodule)
        ├── customBox (submodule)
        ├── docs (submodule)
        ├── generated
        ├── stm32h755_integration (submodule)
        ├── .clang-format
        └── CMakeLists.txt

    #. `build <https://github.com/CosmOS-Creators/reference_project_stmIDE/tree/master/Cosmos/build>`_
        This directory contains all build related files for the C code e.g. system and tests build.
        These CMakeLists.txt files are stored under system or tests directories and included to the
        CMakeLists.txt under the build directory directly. In the toolchain directory are files needed
        for the architecture specific compiling of the system source code and also for the tests.
        The bash script build.sh was created for the system and test build inside the dev docker container
        environment.

    #. `configuration <https://github.com/CosmOS-Creators/reference_project_stmIDE/tree/master/Cosmos/configuration>`_
        This directory contains all workspace and file generation config files together with the systemDefinition directory.
        In the systemDefinition directory we can find two subfolders, one is for the core and one for
        the system specific configuration. These are used during the model creation and generation of the unit configuration
        source code.

    #. `core (submodule) <https://github.com/CosmOS-Creators/core>`_
        This directory contains multiple kernels and support modules (e.g., operating system runtime specific dynamic allocation implementations),
        which consist of smaller parts called units. It was designed with a focus on the minimal compiler and microcontroller dependencies.
        To interface with the microcontroller peripherals, it uses CIL APIs.

    #. `customBox (submodule) <https://github.com/CosmOS-Creators/customBox>`_
        In this directory is stored all customBox source code as it is a part of CosmOS, and it is used to configure everything that is changeable in the system.
        The UI is a generalized skeleton that will dynamically adjust depending on the configuration input.

    #. `docs (submodule) <https://github.com/CosmOS-Creators/docs>`_
        This directory contains documentation for the CosmOS project.

    #. `generated (submodule) <https://github.com/CosmOS-Creators/reference_project_stmIDE/tree/master/Cosmos/generated>`_
        The generated directory contains three folders - application, build and core. Application folder contains generated code that is a part of the
        application layer and user can directly implement his code inside this directory in the specified places. Build folder is used during the system and
        tests builds. The core folder contains generated configuration of the operating system units. In the generated directory could be eventually also folder
        for the generated linker script files, but to stay compliant with the STM IDE project structure these files are generated to the default place.

    #. `stm32h755_integration (submodule) <https://github.com/CosmOS-Creators/stm32h755_integration_HAL>`_
        This directory contains CIL source code and all microcontroller dependent configuration. CosmOS Integration alias CIL is a type of microcontroller abstraction layer.
        It provides a set of APIs required by the core layer in this case specifically for the microcontroller stm32h755 using HAL APIs.

    #. `.clang-format <https://github.com/CosmOS-Creators/reference_project_stmIDE/blob/master/Cosmos/.clang-format>`_
        Clang format file contains configuration for the clang formatter that is used within the CosmOS C/C++ source code.

    #. `CMakeLists.txt <https://github.com/CosmOS-Creators/reference_project_stmIDE/blob/master/Cosmos/CMakeLists.txt>`_
        CMakeLists used during the system and tests builds.
